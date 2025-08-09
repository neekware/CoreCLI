"""Completion definitions for package commands."""


def get_package_completions(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Get completions for package commands.

    Args:
        ctx: Click context
        args: Already provided arguments
        incomplete: Current incomplete word

    Returns:
        List of completion suggestions
    """
    # Get the subcommand if specified
    if not args or args[0] == "package":
        # Suggest package subcommands
        commands = ["build", "dist", "list"]
        return [cmd for cmd in commands if cmd.startswith(incomplete)]

    subcommand = args[0] if args else None

    if subcommand == "build":
        return complete_build(ctx, args[1:], incomplete)
    elif subcommand == "dist":
        return complete_dist(ctx, args[1:], incomplete)
    elif subcommand == "list":
        return complete_list(ctx, args[1:], incomplete)

    return []


def complete_build(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for package build command."""
    if incomplete.startswith("-"):
        options = ["--format", "--output", "--version"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --format
    if args and args[-1] == "--format":
        formats = ["wheel", "sdist", "tar", "zip", "deb", "rpm"]
        return [f for f in formats if f.startswith(incomplete)]

    return []


def complete_dist(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for package dist command."""
    if incomplete.startswith("-"):
        options = ["--upload", "--repository", "--sign"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --repository
    if args and args[-1] == "--repository":
        repos = ["pypi", "testpypi", "local", "private"]
        return [r for r in repos if r.startswith(incomplete)]

    return []


def complete_list(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for package list command."""
    if incomplete.startswith("-"):
        options = ["--installed", "--available", "--outdated", "--format"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --format
    if args and args[-1] == "--format":
        formats = ["table", "json", "yaml", "csv"]
        return [f for f in formats if f.startswith(incomplete)]

    return []


# Export completion registry
COMPLETIONS = {
    "package": get_package_completions,
    "build": complete_build,
    "dist": complete_dist,
    "list": complete_list,
}
