"""Development commands router"""

import click

from commands.subs.dev.all import all
from commands.subs.dev.completion import completion
from commands.subs.dev.format import format
from commands.subs.dev.lint import lint
from commands.subs.dev.precommit import precommit
from commands.subs.dev.test import test
from commands.subs.dev.typecheck import typecheck


@click.group()
def dev() -> None:
    """Development tools"""
    pass


# Add subcommands
dev.add_command(format)
dev.add_command(lint)
dev.add_command(typecheck)
dev.add_command(test)
dev.add_command(all)
dev.add_command(precommit)
dev.add_command(completion)
