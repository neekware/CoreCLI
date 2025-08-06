"""Type checking command"""

import subprocess
import sys

import click


@click.command()
def typecheck() -> None:
    """Type check with mypy"""
    # Only check commands directory (tools may not have Python files)
    cmd = ["mypy", "commands"]
    click.echo(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
