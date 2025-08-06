"""Code linting command"""

import subprocess
import sys

import click


@click.command()
@click.option("--fix", is_flag=True, help="Fix issues automatically")
def lint(fix: bool) -> None:
    """Lint code with ruff"""
    cmd = ["ruff", "check", "."]
    if fix:
        cmd.append("--fix")

    click.echo(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
