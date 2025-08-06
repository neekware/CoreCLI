"""Project management router"""

import click

from commands.subs.proj.info import info
from commands.subs.proj.size import size
from commands.subs.proj.stats import stats


@click.group()
def proj() -> None:
    """Project management commands"""
    pass


# Add subcommands
proj.add_command(info)
proj.add_command(size)
proj.add_command(stats)
