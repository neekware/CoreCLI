# Core CLI

[![CI](https://github.com/neekware/CoreCLI/actions/workflows/test.yml/badge.svg)](https://github.com/neekware/CoreCLI/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue)](https://github.com/python/mypy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python project starter that provides a production-ready CLI out of the box, letting you focus on your core logic instead of boilerplate.

A clean, modular command-line interface demonstrating best practices in CLI development.

## 🎯 Getting Started

### Use This as Your Project Template

```bash
# 1. Clone this repository
git clone https://github.com/neekware/CoreCLI.git myproject
cd myproject

# 2. Remove the original git history
rm -rf .git

# 3. Initialize your own repository
git init
git add .
git commit -m "Initial commit from CoreCLI template"

# 4. Update project details
# Edit pyproject.toml:
#   - Change 'name' from "core-cli" to "myproject-cli"
#   - Update description, authors, etc.

# 5. Add your business logic to src/
mkdir -p src/myproject
touch src/myproject/__init__.py
# Add your core functionality here

# 6. Create CLI commands in commands/subs/
# See commands/subs/proj.py and dev.py for examples

# 7. Update the CLI name (optional)
# In pyproject.toml [project.scripts], change:
# mycli = "commands.main:main"  # Instead of 'cli'
```


### Project Layout

```
myproject/
├── src/                 # YOUR BUSINESS LOGIC GOES HERE
│   └── myproject/      # Your Python package
│       ├── __init__.py
│       ├── core.py     # Core functionality
│       ├── models.py   # Data models
│       └── utils.py    # Utilities
├── commands/           # CLI commands (keep these separate)
│   ├── subs/          # Subcommand modules
│   │   ├── proj.py    # Example: project commands
│   │   ├── dev.py     # Example: dev tools
│   │   └── myapp.py   # YOUR CLI COMMANDS GO HERE
│   └── main.py        # CLI entry point (router)
├── tests/             # Your tests
├── setup.sh           # One-command setup
└── pyproject.toml     # Project configuration
```

## 📋 Table of Contents

- [Getting Started](#-getting-started)
- [Quick Start](#-quick-start)
- [Features](#-features)
- [Development](#-development)
- [Architecture](#-architecture)
- [Versioning](#-versioning)
- [License](#-license)

## 🚀 Quick Start

```bash
# Setup (installs dependencies and pre-commit hooks)
./setup.sh

# Activate the virtual environment
source .venv/bin/activate

# Now use 'cli' directly
cli --help
cli proj -s                # Show repository size
cli dev -a                 # Run all code checks
```

## ✨ Features

- 🧩 **Modular Architecture**: Each command group in its own module
- 🔧 **Development Tools**: Integrated linting (ruff), formatting (black), and type checking (mypy)
- 🔒 **Pre-commit Hooks**: Automatic code quality checks before commits
- 🎯 **Auto-setup**: Virtual environment and dependencies managed automatically
- 🐍 **Type-Safe**: Full type annotations with strict mypy checking
- 📦 **Zero Config**: Works out of the box with sensible defaults
- 🚀 **Production Ready**: Best practices baked in from the start

## 📋 Requirements

- Python 3.9 or higher
- Git (for pre-commit hooks)
- Unix-like environment (Linux, macOS, WSL)

## 🛠️ Development

```bash
# Format code
cli dev -f

# Run linter
cli dev -l

# Type check
cli dev -t

# Run all checks
cli dev -a
```

Pre-commit hooks run automatically on `git commit`.

## 🏗️ Architecture

See [commands/README.md](commands/README.md) for detailed architecture documentation.

## 📌 Versioning

Version is managed in `commands/__version__.py`. To update:

```python
# commands/__version__.py
__version__ = "1.0.0"  # Update this
```

Access version in your code:
```python
from commands import __version__
print(f"Version: {__version__}")
```

The version is automatically used in:
- `cli --version`
- Package metadata
- PyPI uploads (if you publish)

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

### 🙏 Attribution

If your project is public and you found CoreCLI helpful, we'd appreciate a mention like:
> This project was bootstrapped with [CoreCLI](https://github.com/neekware/CoreCLI)


---

Developed with ❤️ by [Val Neekman](https://github.com/un33k) @ [Neekware Inc.](https://neekware.com)
