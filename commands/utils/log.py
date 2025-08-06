def log_info(message: str) -> None:
    """Log info message with green color"""
    print(f"\033[0;32m[INFO]\033[0m {message}")


def log_error(message: str) -> None:
    """Log error message with red color"""
    print(f"\033[0;31m[ERROR]\033[0m {message}")
