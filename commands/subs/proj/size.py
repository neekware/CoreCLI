"""Repository size command"""

import subprocess
from pathlib import Path

import click


@click.command()
def size() -> None:
    """Show repository size"""
    project_root = Path(__file__).parent.parent.parent.parent

    try:
        # Use du command to get directory size
        # -s: summarize, -h: human readable
        result = subprocess.run(
            ["du", "-sh", str(project_root)],
            capture_output=True,
            text=True,
            check=True,
        )

        # Output format is "size\tpath", we want just the size
        size_value = result.stdout.strip().split("\t")[0]
        click.echo(f"Repository size: {size_value}")

    except subprocess.CalledProcessError as e:
        click.echo(f"Error getting repository size: {e}", err=True)
