"""Completion definitions for release commands."""

import subprocess


def get_release_completions(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Get completions for release commands.

    Args:
        ctx: Click context
        args: Already provided arguments
        incomplete: Current incomplete word

    Returns:
        List of completion suggestions
    """
    # Get the subcommand if specified
    if not args or args[0] == "release":
        # Suggest release subcommands
        commands = ["create", "publish", "list"]
        return [cmd for cmd in commands if cmd.startswith(incomplete)]

    subcommand = args[0] if args else None

    if subcommand == "create":
        return complete_create(ctx, args[1:], incomplete)
    elif subcommand == "publish":
        return complete_publish(ctx, args[1:], incomplete)
    elif subcommand == "list":
        return complete_list(ctx, args[1:], incomplete)

    return []


def complete_create(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for release create command."""
    if incomplete.startswith("-"):
        options = ["--version", "--tag", "--branch", "--draft", "--prerelease"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --version
    if args and args[-1] == "--version":
        # Suggest semantic version patterns
        suggestions = ["major", "minor", "patch", "1.0.0", "0.1.0"]
        return [s for s in suggestions if s.startswith(incomplete)]

    # If previous arg was --branch
    if args and args[-1] == "--branch":
        # Try to get git branches
        try:
            result = subprocess.run(
                ["git", "branch", "--format=%(refname:short)"],
                capture_output=True,
                text=True,
                timeout=2,
            )
            if result.returncode == 0:
                branches = result.stdout.strip().split("\n")
                return [b for b in branches if b.startswith(incomplete)]
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
        return ["main", "master", "develop"]

    return []


def complete_publish(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for release publish command."""
    if incomplete.startswith("-"):
        options = ["--platform", "--channel", "--sign", "--verify"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --platform
    if args and args[-1] == "--platform":
        platforms = ["github", "pypi", "npm", "docker", "all"]
        return [p for p in platforms if p.startswith(incomplete)]

    # If previous arg was --channel
    if args and args[-1] == "--channel":
        channels = ["stable", "beta", "alpha", "nightly", "latest"]
        return [c for c in channels if c.startswith(incomplete)]

    return []


def complete_list(ctx: object, args: list[str], incomplete: str) -> list[str]:
    """Completions for release list command."""
    if incomplete.startswith("-"):
        options = ["--all", "--latest", "--limit", "--format"]
        return [opt for opt in options if opt.startswith(incomplete)]

    # If previous arg was --format
    if args and args[-1] == "--format":
        formats = ["table", "json", "yaml", "markdown"]
        return [f for f in formats if f.startswith(incomplete)]

    # If previous arg was --limit
    if args and args[-1] == "--limit":
        limits = ["5", "10", "20", "50", "100"]
        return [limit for limit in limits if limit.startswith(incomplete)]

    return []


# Export completion registry
COMPLETIONS = {
    "release": get_release_completions,
    "create": complete_create,
    "publish": complete_publish,
    "list": complete_list,
}
