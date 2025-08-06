"""Code formatting command"""

import subprocess
import sys

import click


@click.command()
@click.option("--check", is_flag=True, help="Check only, don't modify files")
def format(check: bool) -> None:
    """Format code with black"""
    cmd = ["black", "."]
    if check:
        cmd.append("--check")

    click.echo(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
