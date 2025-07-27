"""Project-related CLI commands"""

import argparse
import os
import subprocess
from pathlib import Path
from typing import TYPE_CHECKING, Any, Union

if TYPE_CHECKING:
    pass


class ProjectCommands:
    """Commands for project management and information"""

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def get_repo_size(self) -> str:
        """Get the size of the repository"""
        try:
            # Use du command to get directory size
            # -s: summarize, -h: human readable
            result = subprocess.run(
                ["du", "-sh", str(self.project_root)],
                capture_output=True,
                text=True,
                check=True,
            )

            # Output format is "size\tpath", we want just the size
            size = result.stdout.strip().split("\t")[0]
            return size

        except subprocess.CalledProcessError as e:
            return f"Error getting repository size: {e}"

    def get_git_info(self) -> dict[str, Union[str, bool]]:
        """Get basic git repository information"""
        info: dict[str, Union[str, bool]] = {}

        try:
            # Get current branch
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.project_root,
            )
            info["branch"] = result.stdout.strip()

            # Get number of commits
            result = subprocess.run(
                ["git", "rev-list", "--count", "HEAD"],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.project_root,
            )
            info["commits"] = result.stdout.strip()

            # Check for uncommitted changes
            result = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.project_root,
            )
            info["has_changes"] = bool(result.stdout.strip())

        except subprocess.CalledProcessError:
            info["error"] = "Not a git repository or git not available"

        return info

    def get_stats(self) -> dict[str, Union[str, int, list[tuple[str, int]]]]:
        """Get detailed repository statistics"""
        stats: dict[str, Union[str, int, list[tuple[str, int]]]] = {}

        try:
            # Count files by extension
            file_counts: dict[str, int] = {}
            total_files = 0
            total_lines = 0

            # Walk through all files
            for root, dirs, files in os.walk(self.project_root):
                # Skip hidden directories and common ignore patterns
                dirs[:] = [
                    d
                    for d in dirs
                    if not d.startswith(".")
                    and d not in ["node_modules", "__pycache__"]
                ]

                for file in files:
                    if file.startswith("."):
                        continue

                    total_files += 1
                    ext = Path(file).suffix or "no extension"
                    file_counts[ext] = file_counts.get(ext, 0) + 1

                    # Try to count lines for text files
                    if ext in [
                        ".py",
                        ".js",
                        ".ts",
                        ".rs",
                        ".go",
                        ".c",
                        ".cpp",
                        ".h",
                        ".java",
                        ".rb",
                        ".sh",
                        ".md",
                        ".txt",
                    ]:
                        try:
                            file_path = os.path.join(root, file)
                            with open(
                                file_path, encoding="utf-8", errors="ignore"
                            ) as f:
                                lines = len(f.readlines())
                                total_lines += lines
                        except Exception:
                            pass

            stats["total_files"] = total_files
            stats["total_lines"] = total_lines
            stats["file_types"] = sorted(
                file_counts.items(), key=lambda x: x[1], reverse=True
            )[
                :10
            ]  # Top 10

            # Get directory count
            dir_count = sum(
                1
                for _, dirs, _ in os.walk(self.project_root)
                for d in dirs
                if not d.startswith(".")
            )
            stats["total_directories"] = dir_count

        except Exception as e:
            stats["error"] = f"Error gathering statistics: {e}"

        return stats

    @staticmethod
    def add_subparser(
        subparsers: "argparse._SubParsersAction[Any]",
    ) -> argparse.ArgumentParser:
        """Add project subcommands to argument parser"""
        proj_parser = subparsers.add_parser("proj", help="Project management commands")

        # Add flags (not subcommands) for different operations
        proj_parser.add_argument(
            "-s", "--size", action="store_true", help="Show repository size"
        )
        proj_parser.add_argument(
            "-i", "--info", action="store_true", help="Show project information"
        )
        # Example: --super-fast has no short form because -s is taken by --size
        proj_parser.add_argument(
            "--stats",
            action="store_true",
            help="Show detailed statistics (no short form, -s taken by --size)",
        )

        return proj_parser  # type: ignore[no-any-return]
