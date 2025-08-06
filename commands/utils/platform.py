"""Platform detection utilities for commands"""

import platform


def get_current_target_arch() -> tuple[str, str]:
    """Get current system's target and architecture

    Returns:
        Tuple of (target, arch) where:
        - target: 'darwin', 'linux', or 'windows'
        - arch: 'arm64' or 'amd64'

    Example:
        target, arch = get_current_target_arch()
        # On macOS ARM64: ('darwin', 'arm64')
        # On Linux x86_64: ('linux', 'amd64')
    """
    # Get system name
    system = platform.system().lower()
    if system == "darwin":
        target = "darwin"
    elif system == "linux":
        target = "linux"
    elif system == "windows":
        target = "windows"
    else:
        # Default to linux for unknown systems
        target = "linux"

    # Get machine architecture
    machine = platform.machine().lower()
    if machine in ("arm64", "aarch64"):
        arch = "arm64"
    elif machine in ("x86_64", "amd64", "x64"):
        arch = "amd64"
    elif machine in ("i386", "i686", "x86"):
        # 32-bit systems map to amd64 as closest supported
        arch = "amd64"
    else:
        # Default to arm64 for unknown architectures
        arch = "arm64"

    return target, arch


def get_current_platform() -> str:
    """Get current platform as 'target-arch' string

    Returns:
        Platform string like 'darwin-arm64', 'linux-amd64', etc.
    """
    target, arch = get_current_target_arch()
    return f"{target}-{arch}"
