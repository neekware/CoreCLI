"""Pre-commit checks command"""

import subprocess
import sys
from pathlib import Path

import click


@click.command()
@click.option("--fix", is_flag=True, help="Automatically fix issues where possible")
@click.option(
    "--ci", is_flag=True, help="Run in CI mode (check all files, not just staged)"
)
def precommit(fix: bool, ci: bool) -> None:
    """Run all pre-commit checks locally

    This runs the same checks as the actual pre-commit hooks:
    - Black formatting (always applied to ensure consistency)
    - Ruff linting (--fix to auto-fix)
    - MyPy type checking
    - Rust formatting and checks
    - Tests (when --ci flag is used)

    By default, runs on staged files only. Use --ci to check ALL files like CI does.
    Use --fix to automatically fix Ruff issues (Black always formats).
    """
    project_root = Path(__file__).parent.parent.parent

    # Track if any changes were made
    any_changes = False
    any_failures = False

    if ci:
        click.echo("🔍 Running CI checks (all files)...\n")
    else:
        click.echo("🔍 Running pre-commit checks...\n")

    # 1. Always format with Black first (to ensure consistent formatting)
    click.echo("📝 Formatting with Black...")
    black_cmd = ["black", "."]
    result = subprocess.run(black_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        click.echo("   ✗ Black formatting failed")
        if result.stdout:
            click.echo(result.stdout)
        if result.stderr:
            click.echo(result.stderr)
        any_failures = True
    else:
        if "reformatted" in result.stdout:
            click.echo("   ✓ Black reformatted files")
            any_changes = True
        else:
            click.echo("   ✓ Black: all files already formatted")

    # 2. Ruff linting
    click.echo("\n🔍 Running Ruff linter...")
    ruff_cmd = ["ruff", "check", "."]
    if fix:
        ruff_cmd.append("--fix")
    result = subprocess.run(ruff_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        if fix and "fixed" in result.stdout:
            click.echo("   ✓ Ruff fixed issues")
            any_changes = True
        else:
            click.echo(
                "   ✗ Ruff found issues" + (" (run with --fix)" if not fix else "")
            )
            if result.stdout:
                click.echo(result.stdout)
            any_failures = True
    else:
        click.echo("   ✓ Ruff: all good")

    # 3. MyPy type checking (on specific directories)
    click.echo("\n📊 Running MyPy type checker...")
    mypy_cmd = ["mypy", "commands", "--config-file", "pyproject.toml"]
    result = subprocess.run(mypy_cmd, capture_output=True, text=True)
    if result.returncode != 0:
        click.echo("   ✗ MyPy found type errors")
        if result.stdout:
            click.echo(result.stdout)
        any_failures = True
    else:
        click.echo("   ✓ MyPy: all good")

    # 4. Run tests if in CI mode
    if ci:
        click.echo("\n🧪 Running tests...")
        test_cmd = ["pytest", "commands/tests/"]
        result = subprocess.run(test_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            click.echo("   ✗ Tests failed")
            if result.stdout:
                click.echo(result.stdout)
            if result.stderr:
                click.echo(result.stderr)
            any_failures = True
        else:
            click.echo("   ✓ Tests: all passed")

    # 5. Check if there are Rust files changed
    rust_files = list(project_root.glob("rust/**/*.rs"))
    if rust_files:
        # 4a. Rust formatting
        click.echo("\n🦀 Running Rust formatter...")
        rust_fmt_cmd = [sys.executable, "-m", "commands", "rust", "all"]
        if fix:
            rust_fmt_cmd.append("--fix")
        result = subprocess.run(rust_fmt_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            click.echo("   ✗ Rust format failed")
            if result.stdout:
                click.echo(result.stdout)
            any_failures = True
        else:
            if fix and "Formatted" in result.stdout:
                click.echo("   ✓ Rust files formatted")
                any_changes = True
            else:
                click.echo("   ✓ Rust format: all good")

        # 4b. Rust check
        click.echo("\n🦀 Running Rust check...")
        rust_check_cmd = [sys.executable, "-m", "commands", "rust", "check"]
        result = subprocess.run(rust_check_cmd, capture_output=True, text=True)
        if result.returncode != 0:
            click.echo("   ✗ Rust check failed")
            if result.stdout:
                click.echo(result.stdout)
            any_failures = True
        else:
            click.echo("   ✓ Rust check: all good")

    # Summary
    click.echo("\n" + "=" * 60)
    if any_failures:
        click.echo("❌ Pre-commit checks failed!")
        if not fix:
            click.echo(
                "\n💡 Tip: Run 'cli dev precommit --fix' to automatically fix issues"
            )
        sys.exit(1)
    elif any_changes:
        click.echo("✅ Pre-commit checks passed (with fixes applied)")
        click.echo(
            "\n⚠️  Files were modified. Remember to stage changes before committing:"
        )
        click.echo("   git add -A")
        click.echo("   git commit -m 'Your message'")
    else:
        click.echo("✅ All pre-commit checks passed!")
        click.echo("\nYou're ready to commit! 🎉")
