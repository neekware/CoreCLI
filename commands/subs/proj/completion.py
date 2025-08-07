"""Completion definitions for proj commands."""


def get_proj_completions(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Get completions for proj commands.

    Args:
        ctx: Click context
        args: Already provided arguments
        incomplete: Current incomplete word

    Returns:
        List of completion suggestions
    """
    # Get the subcommand if specified
    if not args or args[0] == "proj":
        # Suggest proj subcommands
        commands = ["info", "size", "stats"]
        return [cmd for cmd in commands if cmd.startswith(incomplete)]

    # No special completions for proj subcommands yet
    return []


def complete_info(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for proj info command."""
    # info takes no arguments
    return []


def complete_size(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for proj size command."""
    # size takes no arguments
    return []


def complete_stats(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for proj stats command."""
    # stats takes no arguments
    return []


# Export completion registry
COMPLETIONS = {
    "proj": get_proj_completions,
    "info": complete_info,
    "size": complete_size,
    "stats": complete_stats,
}
