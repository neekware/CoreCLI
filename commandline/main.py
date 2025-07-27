#!/usr/bin/env python3
"""CLI - Main entry point"""

import argparse
from pathlib import Path

from . import __version__
from .commands.dev import DevCommands
from .commands.proj import ProjectCommands


def main() -> None:
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        prog="cli",
        description="CLI for Shaypoor",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  cli proj -s                  # Show repository size
  cli proj -i                  # Show project information
  cli proj --stats             # Show detailed statistics

  cli dev -f                   # Format code with black
  cli dev -l                   # Lint code with ruff
  cli dev -a                   # Run all checks
        """,
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument("--debug", action="store_true", help="Enable debug output")

    # Add subcommands
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add project commands
    ProjectCommands.add_subparser(subparsers)

    # Add dev commands
    DevCommands.add_subparser(subparsers)

    # Parse arguments
    args = parser.parse_args()

    # Get project root (where cli was called from)
    project_root = Path.cwd()

    # Handle commands
    if args.command == "proj":
        proj_cmd = ProjectCommands(project_root)

        if args.size:
            size = proj_cmd.get_repo_size()
            print(f"Repository size: {size}")
        elif args.info:
            info = proj_cmd.get_git_info()
            if "error" in info:
                print(f"Error: {info['error']}")
            else:
                print(f"Branch: {info.get('branch', 'unknown')}")
                print(f"Total commits: {info.get('commits', 'unknown')}")
                print(
                    f"Uncommitted changes: {'Yes' if info.get('has_changes') else 'No'}"
                )
        elif args.stats:
            stats = proj_cmd.get_stats()
            if "error" in stats:
                print(f"Error: {stats['error']}")
            else:
                print("Repository Statistics:")
                print(f"  Total files: {stats.get('total_files', 0)}")
                print(f"  Total directories: {stats.get('total_directories', 0)}")
                print(f"  Total lines of code: {stats.get('total_lines', 0):,}")

                file_types = stats.get("file_types")
                if file_types and isinstance(file_types, list):
                    print("\nTop file types:")
                    for ext, count in file_types:
                        print(f"    {ext}: {count} files")
        else:
            # No flags provided, show help for proj command
            parser.parse_args(["proj", "--help"])
    elif args.command == "dev":
        dev_cmd = DevCommands(project_root)

        if args.all:
            dev_cmd.run_all_checks()
        elif args.format:
            dev_cmd.format_code(check_only=args.check)
        elif args.lint:
            dev_cmd.lint_code(fix=args.fix)
        elif args.type_check:
            dev_cmd.type_check()
        elif args.pre_commit:
            dev_cmd.setup_pre_commit(uninstall=args.uninstall)
        else:
            # No flags provided, show help for dev command
            parser.parse_args(["dev", "--help"])
    else:
        # No command provided, show main help
        parser.print_help()


if __name__ == "__main__":
    main()
