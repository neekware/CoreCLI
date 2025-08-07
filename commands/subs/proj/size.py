"""Repository size command"""

import subprocess

import click

from commands.utils.paths import get_paths


@click.command()
def size() -> None:
    """Show repository size"""
    project_root = get_paths().root

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
