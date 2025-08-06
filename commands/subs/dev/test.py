"""Testing command"""

import subprocess
import sys

import click


@click.command()
def test() -> None:
    """Run pytest"""
    cmd = ["pytest", "-v"]
    click.echo(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
