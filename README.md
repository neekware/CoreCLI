# Core CLI

[![CI](https://github.com/neekware/CoreCLI/actions/workflows/test.yml/badge.svg)](https://github.com/neekware/CoreCLI/actions/workflows/test.yml)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue)](https://github.com/python/mypy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python project starter that provides a production-ready CLI out of the box, letting you focus on your core logic instead of boilerplate.

A clean, modular command-line interface demonstrating best practices in CLI development.

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Development](#-development)
- [Architecture](#-architecture)
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

## 📁 Project Structure

```
├── commandline/           # CLI implementation
│   ├── commands/         # Subcommand modules
│   │   ├── proj.py      # Project info commands
│   │   ├── dev.py       # Development tools
│   │   └-- next.py      # Your next commands here
│   └── main.py          # CLI entry point
├── setup.sh             # One-command setup
└── pyproject.toml       # Project configuration
```

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

See [commandline/README.md](commandline/README.md) for detailed architecture documentation.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

Developed by [Val Neekman](https://github.com/un33k) @ [Neekware Inc.](https://neekware.com)
