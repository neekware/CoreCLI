"""Development tools CLI commands"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any


class DevCommands:
    """Commands for development tools like linting and formatting"""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def run_command(self, cmd: list[str], description: str) -> tuple[bool, str]:
        """Run a command and return success status and output"""
        try:
            result = subprocess.run(
                cmd, capture_output=True, text=True, cwd=self.project_root
            )

            if result.returncode == 0:
                return True, result.stdout
            else:
                return False, result.stderr or result.stdout

        except FileNotFoundError:
            return False, f"{cmd[0]} not found. Run: pip install -e '.[dev]'"
        except Exception as e:
            return False, str(e)

    def format_code(self, check_only: bool = False) -> None:
        """Run black formatter on the codebase"""
        cmd = ["black", "."]
        if check_only:
            cmd.append("--check")
            print("Checking code formatting...")
        else:
            print("Formatting code...")

        success, output = self.run_command(cmd, "black")

        if check_only and not success:
            print("❌ Code formatting issues found. Run: cli dev --format")
            if output:
                print(output)
            sys.exit(1)
        elif success:
            print("✅ Code formatting OK" if check_only else "✅ Code formatted")
        else:
            print(f"❌ Error: {output}")
            sys.exit(1)

    def lint_code(self, fix: bool = False) -> None:
        """Run ruff linter on the codebase"""
        cmd = ["ruff", "check", "."]
        if fix:
            cmd.append("--fix")
            print("Linting and fixing code...")
        else:
            print("Linting code...")

        success, output = self.run_command(cmd, "ruff")

        if not success and not fix:
            print("❌ Linting issues found. Run: cli dev --lint --fix")
            if output:
                print(output)
            sys.exit(1)
        elif success:
            print("✅ No linting issues found")
        else:
            print(f"❌ Error: {output}")
            sys.exit(1)

    def type_check(self) -> None:
        """Run mypy type checker"""
        print("Type checking code...")

        # Run mypy on the commandline package
        cmd = ["mypy", "commandline"]
        success, output = self.run_command(cmd, "mypy")

        if success:
            print("✅ Type checking passed")
            if output:
                print(output)
        else:
            print("❌ Type checking failed")
            print(output)
            sys.exit(1)

    def run_all_checks(self) -> None:
        """Run all checks (format check, lint, type check)"""
        print("Running all checks...\n")

        # Format check (don't modify)
        self.format_code(check_only=True)
        print()

        # Lint check
        self.lint_code(fix=False)
        print()

        # Type check
        self.type_check()

        print("\n✅ All checks passed!")

    def setup_pre_commit(self, uninstall: bool = False) -> None:
        """Install or uninstall pre-commit hooks"""
        if uninstall:
            print("Uninstalling pre-commit hooks...")
            cmd = ["pre-commit", "uninstall"]
        else:
            print("Installing pre-commit hooks...")
            cmd = ["pre-commit", "install"]

        success, output = self.run_command(cmd, "pre-commit")

        if success:
            action = "uninstalled" if uninstall else "installed"
            print(f"✅ Pre-commit hooks {action}")
            if not uninstall:
                print("Hooks will run automatically on git commit")
        else:
            print(f"❌ Error: {output}")
            sys.exit(1)

    @staticmethod
    def add_subparser(
        subparsers: "argparse._SubParsersAction[Any]",
    ) -> argparse.ArgumentParser:
        """Add dev subcommands to argument parser"""
        dev_parser = subparsers.add_parser("dev", help="Development tools")

        # Add flags for different operations
        dev_parser.add_argument(
            "-f", "--format", action="store_true", help="Format code with black"
        )
        dev_parser.add_argument(
            "-l", "--lint", action="store_true", help="Lint code with ruff"
        )
        dev_parser.add_argument(
            "-t", "--type-check", action="store_true", help="Type check with mypy"
        )
        dev_parser.add_argument(
            "-a", "--all", action="store_true", help="Run all checks"
        )
        dev_parser.add_argument(
            "-p", "--pre-commit", action="store_true", help="Install pre-commit hooks"
        )

        # Modifiers
        dev_parser.add_argument(
            "--check", action="store_true", help="Check only, don't modify (for format)"
        )
        dev_parser.add_argument(
            "--fix", action="store_true", help="Fix issues automatically (for lint)"
        )
        dev_parser.add_argument(
            "--uninstall", action="store_true", help="Uninstall pre-commit hooks"
        )

        return dev_parser  # type: ignore[no-any-return]
