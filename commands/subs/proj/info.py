"""Project information command"""

import subprocess

import click

from commands.utils.paths import get_paths


@click.command()
def info() -> None:
    """Show project information"""
    project_root = get_paths().root

    click.echo(f"Project root: {project_root}")

    # Get git info
    try:
        # Get current branch
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=project_root,
        )
        branch = result.stdout.strip()

        # Get number of commits
        result = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
            cwd=project_root,
        )
        commits = result.stdout.strip()

        # Check for uncommitted changes
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True,
            cwd=project_root,
        )
        has_changes = bool(result.stdout.strip())

        click.echo(f"Git branch: {branch}")
        click.echo(f"Total commits: {commits}")
        click.echo(f"Uncommitted changes: {'Yes' if has_changes else 'No'}")

    except subprocess.CalledProcessError:
        click.echo("Not a git repository or git not available", err=True)
