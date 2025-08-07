"""Path resolver utility for consistent project root detection across all commands"""

from pathlib import Path
from typing import Optional


def get_project_root() -> Path:
    """Get the project root directory reliably.

    This works from anywhere in the project by looking for key markers.
    Traverses up from the current file location until it finds the project root.

    Returns:
        Path: The absolute path to the project root directory

    Raises:
        RuntimeError: If project root cannot be found
    """
    current = Path(__file__).resolve().parent

    # Go up until we find the project root markers
    # We look for pyproject.toml and commands directory as markers
    while current != current.parent:
        if (current / "pyproject.toml").exists() and (current / "commands").exists():
            return current
        current = current.parent

    # If we can't find it from file location, try from CWD
    current = Path.cwd().resolve()
    while current != current.parent:
        if (current / "pyproject.toml").exists() and (current / "commands").exists():
            return current
        current = current.parent

    # Fallback - should not happen in normal use
    raise RuntimeError(
        "Could not find project root. Make sure you're running from within the project directory."
    )


class ProjectPaths:
    """Centralized path management for the project.

    Provides consistent access to common project directories.
    """

    def __init__(self, root: Optional[Path] = None):
        """Initialize ProjectPaths.

        Args:
            root: Optional project root path. If not provided, will auto-detect.
        """
        self.root = root if root else get_project_root()

    @property
    def commands_dir(self) -> Path:
        """Get the commands directory."""
        return self.root / "commands"

    @property
    def tools_dir(self) -> Path:
        """Get the tools directory."""
        return self.root / "tools"

    @property
    def src_dir(self) -> Path:
        """Get the src directory (for user code)."""
        return self.root / "src"

    @property
    def tests_dir(self) -> Path:
        """Get the tests directory."""
        return self.root / "tests"

    @property
    def build_dir(self) -> Path:
        """Get the build directory."""
        return self.root / "build"

    @property
    def dist_dir(self) -> Path:
        """Get the dist directory."""
        return self.root / "dist"

    @property
    def cache_dir(self) -> Path:
        """Get the cache directory."""
        return self.root / ".cache"

    @property
    def venv_dir(self) -> Path:
        """Get the virtual environment directory."""
        return self.root / ".venv"

    @property
    def docs_dir(self) -> Path:
        """Get the documentation directory."""
        return self.root / "docs"

    @property
    def assets_dir(self) -> Path:
        """Get the assets directory."""
        return self.root / "assets"

    def ensure_directory(self, path: Path) -> Path:
        """Ensure a directory exists, creating it if necessary.

        Args:
            path: The directory path to ensure exists

        Returns:
            Path: The directory path
        """
        path.mkdir(parents=True, exist_ok=True)
        return path

    def ensure_build_directories(self) -> None:
        """Create all necessary build directories."""
        self.ensure_directory(self.build_dir)
        self.ensure_directory(self.dist_dir)
        self.ensure_directory(self.cache_dir)

    def ensure_src_directories(self) -> None:
        """Create all necessary source directories."""
        self.ensure_directory(self.src_dir)
        self.ensure_directory(self.tests_dir)
        self.ensure_directory(self.docs_dir)

    def get_relative_path(self, absolute_path: Path) -> Path:
        """Get a path relative to the project root.

        Args:
            absolute_path: An absolute path

        Returns:
            Path: The path relative to project root
        """
        try:
            return absolute_path.relative_to(self.root)
        except ValueError:
            # Path is not under project root
            return absolute_path

    def is_in_project(self, path: Path) -> bool:
        """Check if a path is within the project directory.

        Args:
            path: The path to check

        Returns:
            bool: True if the path is within the project
        """
        try:
            path.resolve().relative_to(self.root)
            return True
        except ValueError:
            return False


# Singleton instance
_paths: Optional[ProjectPaths] = None


def get_paths() -> ProjectPaths:
    """Get the singleton ProjectPaths instance.

    Returns:
        ProjectPaths: The singleton instance
    """
    global _paths
    if _paths is None:
        _paths = ProjectPaths()
    return _paths


# Convenience functions
def get_project_root_cached() -> Path:
    """Get the project root using the cached singleton.

    Returns:
        Path: The project root directory
    """
    return get_paths().root


def ensure_in_project_root() -> None:
    """Ensure we're running from the project root directory.

    Raises:
        RuntimeError: If not in project root
    """
    paths = get_paths()
    if Path.cwd().resolve() != paths.root:
        raise RuntimeError(
            f"This command must be run from the project root directory: {paths.root}\n"
            f"Current directory: {Path.cwd()}"
        )


def get_src_path(*parts: str) -> Path:
    """Get a path within the src directory.

    Args:
        *parts: Path components relative to src directory

    Returns:
        Path: The full path
    """
    return get_paths().src_dir.joinpath(*parts)


def get_build_path(*parts: str) -> Path:
    """Get a path within the build directory.

    Args:
        *parts: Path components relative to build directory

    Returns:
        Path: The full path
    """
    return get_paths().build_dir.joinpath(*parts)
