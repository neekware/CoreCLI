"""Run all development checks command"""

import subprocess
import sys

import click


@click.command()
def all() -> None:
    """Run all checks"""
    click.echo("Running all development checks...\n")

    commands = [
        (["black", "--check", "."], "Formatting check"),
        (["ruff", "check", "."], "Linting"),
        (["mypy", "commands"], "Type checking"),
        (["python", "commands/tests/test_cmd_completion.py"], "Completion tests"),
        (["pytest", "-v"], "Tests"),
    ]

    failed = []
    for cmd, name in commands:
        click.echo("\n" + "=" * 60)
        click.echo("Running " + name + "...")
        click.echo("=" * 60)

        result = subprocess.run(cmd)
        if result.returncode != 0:
            failed.append(name)

    if failed:
        click.echo(f"\n❌ Failed checks: {', '.join(failed)}", err=True)
        sys.exit(1)
    else:
        click.echo("\n✅ All checks passed!")
        sys.exit(0)
