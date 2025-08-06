"""Shell completion management commands"""

import subprocess
import sys
from pathlib import Path

import click


@click.group()
def completion() -> None:
    """Shell completion management"""
    pass


@completion.command(name="test")
def test_completion() -> None:
    """Test shell completion functionality"""
    click.echo("Running completion tests...")
    result = subprocess.run(
        ["python", "commands/tests/test_cmd_completion.py"],
        capture_output=True,
        text=True,
    )

    click.echo(result.stdout)
    if result.stderr:
        click.echo(result.stderr, err=True)

    if result.returncode != 0:
        click.echo("❌ Completion tests failed!", err=True)
        sys.exit(1)
    else:
        click.echo("✅ Completion tests passed!")
        sys.exit(0)


@completion.command()
def sync() -> None:
    """Sync shell completion with current CLI commands"""
    project_root = Path(__file__).parent.parent.parent.parent
    completion_path = project_root / "commands" / "autogen" / "completion.sh"

    # Files to check for changes
    command_files = [
        project_root / "commands" / "main.py",
        *list((project_root / "commands" / "subs").rglob("*.py")),
    ]

    # Check if regeneration is needed
    if completion_path.exists():
        completion_mtime = completion_path.stat().st_mtime
        needs_update = any(
            cmd_file.stat().st_mtime > completion_mtime
            for cmd_file in command_files
            if cmd_file.exists()
        )

        if not needs_update:
            click.echo("✓ Shell completion is already up to date")
            return
    else:
        click.echo("⚠️  Shell completion script not found")

    click.echo("🔄 Regenerating shell completion...")

    try:
        # Import here to avoid circular imports
        sys.path.insert(0, str(project_root))
        from commands.main import cli
        from commands.utils.completion import (
            generate_completion_script,
            get_command_info,
        )

        # Generate completion script
        cli_info = get_command_info(cli)
        completion_script = generate_completion_script(cli_info)

        # Add completion loaded marker
        completion_script = completion_script.replace(
            "# Auto-generated completion script for ehAye™ Core CLI",
            "# Auto-generated completion script for ehAye™ Core CLI\nexport _ehaye_cli_completions_loaded=1",
        )

        # Write to file
        completion_path.write_text(completion_script)

        click.echo(f"✅ Generated {completion_path.relative_to(project_root)}")
        click.echo(
            "💡 Restart your shell or run 'source .venv/bin/activate' to load new completions"
        )

    except Exception as e:
        click.echo(f"❌ Failed to generate completion: {e}", err=True)
        sys.exit(1)
