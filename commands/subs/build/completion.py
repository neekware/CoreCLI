"""Completion definitions for build commands."""


def get_build_completions(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Get completions for build commands.

    Args:
        ctx: Click context
        args: Already provided arguments
        incomplete: Current incomplete word

    Returns:
        List of completion suggestions
    """
    # Get the subcommand if specified
    if not args or args[0] == "build":
        # Suggest build subcommands
        commands = ["all", "clean", "component"]
        return [cmd for cmd in commands if cmd.startswith(incomplete)]

    subcommand = args[0] if args else None

    if subcommand == "component":
        return complete_component(ctx, args[1:], incomplete)
    elif subcommand == "clean":
        return complete_clean(ctx, args[1:], incomplete)

    return []


def complete_all(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for build all command."""
    # Check for flags
    if incomplete.startswith("-"):
        options = ["--parallel", "--clean", "--verbose"]
        return [opt for opt in options if opt.startswith(incomplete)]
    return []


def complete_clean(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for build clean command."""
    # Check for flags
    if incomplete.startswith("-"):
        options = ["--force", "--cache", "--all"]
        return [opt for opt in options if opt.startswith(incomplete)]
    return []


def complete_component(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for build component command."""
    # Suggest available components
    components = ["frontend", "backend", "docs", "tests", "assets"]

    # If no component specified yet
    if not args:
        return [c for c in components if c.startswith(incomplete)]

    # Check for flags
    if incomplete.startswith("-"):
        options = ["--watch", "--debug", "--production"]
        return [opt for opt in options if opt.startswith(incomplete)]

    return []


# Export completion registry
COMPLETIONS = {
    "build": get_build_completions,
    "all": complete_all,
    "clean": complete_clean,
    "component": complete_component,
}
