# 🚀 ehAye™ Core CLI

<div align="center">

[![Python](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue)](https://github.com/python/mypy)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

### **🎓 The Best CLI Framework for AI Developers, Researchers & Students**

**We handle your build environment, so you can focus on your core responsibility.**

Stop wrestling with boilerplate. Start shipping features. ehAye™ Core CLI is the production-ready foundation that lets AI developers, researchers, and students concentrate on what matters: **their actual project**.

[Quick Start](#-quick-start) • [Features](#-features) • [Architecture](#-architecture) • [Commands](#-command-showcase) • [Documentation](#-documentation)

</div>

---

## 🎯 Why ehAye™ Core CLI?

**Perfect for AI Developers & Researchers:** Whether you're building ML pipelines, research tools, or data processing utilities, stop wasting time on CLI infrastructure.

ehAye™ Core CLI is a **batteries-included CLI template** that provides:

- ✅ **Zero Configuration** - Works instantly, no setup headaches
- ✅ **Production Ready** - Type-safe, tested, documented from day one
- ✅ **Best Practices Built-In** - Linting, formatting, testing - all configured
- ✅ **AI Developer Friendly** - Perfect for ML tools, data pipelines, research utilities
- ✅ **Focus on Your Research** - We handle the DevOps, you handle the innovation

## 🚀 Quick Start

Get up and running in less than 60 seconds:

```bash
# 1. Clone the template
git clone https://github.com/neekware/ehAyeCoreCLI.git my-awesome-cli
cd my-awesome-cli

# 2. Customize your project (edit commands/config.py)
# Set PROJECT_NAME = "MyAwesomeCLI"

# 3. Setup and activate
./setup.sh
source .venv/bin/activate

# 4. Start using your CLI!
cli --help
cli proj info
cli dev all
```

That's it! You now have a fully functional CLI with development tools, testing, and documentation.

## 🏗️ Architecture

<div align="center">

```mermaid
graph TD
    A[Your Source Code] -->|Focus Here| B[Your Core Logic]
    B --> CLI[ehAye™ Core CLI Framework]
    
    CLI --> D[Development Tools]
    CLI --> E[Build System]
    CLI --> F[Package Management]
    CLI --> G[Release Pipeline]
    
    D --> D1[Black Formatter]
    D --> D2[Ruff Linter]
    D --> D3[MyPy Type Checker]
    D --> D4[Pytest Runner]
    
    E --> E1[Multi-Platform Builds]
    E --> E2[Architecture Support]
    E --> E3[Debug/Release Modes]
    
    F --> F1[Wheel/Sdist Creation]
    F --> F2[PyPI Publishing]
    F --> F3[Dependency Management]
    
    G --> G1[Version Management]
    G --> G2[GitHub Releases]
    G --> G3[Docker Images]
    
    style A fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#000
    style B fill:#C8E6C9,stroke:#2E7D32,stroke-width:3px,color:#000
    style CLI fill:#BBDEFB,stroke:#1565C0,stroke-width:2px,color:#000
    style D fill:#FFE0B2,stroke:#F57C00,stroke-width:2px,color:#000
    style E fill:#FFE0B2,stroke:#F57C00,stroke-width:2px,color:#000
    style F fill:#FFE0B2,stroke:#F57C00,stroke-width:2px,color:#000
    style G fill:#FFE0B2,stroke:#F57C00,stroke-width:2px,color:#000
```

**Your responsibility:** Write your application logic  
**Our responsibility:** Everything else - testing, linting, building, packaging, releasing

</div>

## ✨ Features

### 🧩 Modular Command Architecture
Each command group lives in its own module. Add new commands by creating a file in `commands/subs/`:

```python
# commands/subs/hello.py
import click

@click.group()
def hello() -> None:
    """Hello world commands"""
    pass

@hello.command()
def world() -> None:
    """Say hello to the world"""
    click.echo("Hello, World! 🌍")
```

### 🔧 Professional Development Tools
Built-in development commands that enforce code quality:

```bash
cli dev format     # Auto-format with Black
cli dev lint       # Lint with Ruff
cli dev typecheck  # Type check with MyPy
cli dev test       # Run tests with pytest
cli dev all        # Run everything at once
```

### 🎨 Rich Command Examples
Placeholder commands with comprehensive options to learn from:

```bash
# Build commands with platform targeting
cli build all --target linux --arch x86_64 --release

# Package commands with multiple formats
cli package build --format wheel --sign --include-deps

# Release commands with distribution support
cli release create --version 1.0.0 --draft --notes "First release!"
cli release publish --target pypi --skip-tests
```

### 🔒 Type Safety Throughout
Full type annotations with strict MyPy checking:

```python
from typing import Optional, List, Dict
from pathlib import Path

def process_files(
    files: List[Path],
    options: Dict[str, Any],
    output: Optional[Path] = None
) -> bool:
    """Fully typed functions catch errors before runtime"""
    ...
```

### 🎯 Shell Completion
Tab completion that just works:

```bash
cli <TAB>
# Shows: build dev package proj release version

cli dev <TAB>
# Shows: all format lint typecheck test precommit

cli build all --<TAB>
# Shows: --target --arch --force --copy-only --debug --release
```

### 📊 Project Intelligence
Built-in project management commands:

```bash
cli proj info   # Git status, branch info, recent commits
cli proj size   # Repository size analysis
cli proj stats  # File counts, lines of code, language breakdown
```

## 📖 Command Showcase

### Development Workflow

```bash
# Start your day - check project status
$ cli proj info
📊 Project Information
Git branch: main
Status: 3 modified files
Latest commit: 2 hours ago

# Make changes and check quality
$ cli dev all
✅ Black: All formatted
✅ Ruff: No issues
✅ MyPy: Type safe
✅ Tests: 42 passed

# Ready to commit - run pre-commit checks
$ cli dev precommit --fix
✅ All pre-commit checks passed!
```

### Extensible Placeholders

The template includes thoughtfully designed placeholder commands that demonstrate various CLI patterns:

#### Build System
```bash
cli build all --target darwin --arch arm64 --release
cli build clean --force --cache --deps
cli build component my-component --copy-only
```

#### Package Management
```bash
cli package build --format wheel --output ./dist
cli package dist --upload-url https://pypi.org --verify
cli package list --outdated --format json
cli package verify package.whl --check-signature
```

#### Release Automation
```bash
cli release create --version 2.0.0 --tag v2.0.0 --draft
cli release publish --target github --token $GITHUB_TOKEN
cli release list --limit 10
cli release delete 1.0.0-beta --keep-tag
```

## 🏗️ Project Structure

```
your-project/
├── commands/              # CLI implementation
│   ├── config.py         # Project configuration (customize here!)
│   ├── main.py           # CLI entry point
│   ├── subs/             # Command modules
│   │   ├── build/        # Build commands
│   │   ├── dev/          # Development tools
│   │   ├── package/      # Package management
│   │   ├── proj/         # Project utilities
│   │   └── release/      # Release automation
│   ├── utils/            # Shared utilities
│   └── tests/            # Test suite
├── tools/                # Development tools
├── .pre-commit-config.yaml
├── pyproject.toml        # Project configuration
├── setup.sh              # One-command setup
├── LICENSE               # AGPL-3.0
└── README.md            # You are here!
```

## 🛠️ Customization Guide

### 1. Make It Yours

Edit `commands/config.py`:

```python
PROJECT_NAME = "MyCLI"
PROJECT_DESCRIPTION = "My awesome CLI tool"
```

### 2. Add Your Commands

Create new command groups in `commands/subs/`:

```python
# commands/subs/database.py
import click

@click.group()
def database() -> None:
    """Database management commands"""
    pass

@database.command()
@click.option("--host", default="localhost")
def connect(host: str) -> None:
    """Connect to database"""
    click.echo(f"Connecting to {host}...")
```

### 3. Register Commands

Add to `commands/main.py`:

```python
from commands.subs.database import database

cli.add_command(database)
```

## 📋 Requirements

- Python 3.9 or higher
- Git (for pre-commit hooks)
- Unix-like environment (Linux, macOS, WSL)

## 🧪 Testing

The template includes a complete testing setup:

```bash
# Run all tests
cli dev test

# Run specific test file
pytest commands/tests/test_main.py -v

# Run with coverage
pytest --cov=commands --cov-report=html

# Open coverage report
open htmlcov/index.html
```

## 🔍 Pre-commit Hooks

Quality checks run automatically on every commit:

- **Black** - Code formatting
- **Ruff** - Fast Python linting
- **MyPy** - Static type checking

Run manually anytime:

```bash
cli dev precommit        # Check staged files
cli dev precommit --fix  # Auto-fix issues
cli dev precommit --ci   # Check all files
```

## 📚 Documentation

- [CLAUDE.md](CLAUDE.md) - Development guidelines and conventions
- [Commands Reference](#-command-showcase) - Detailed command documentation
- [API Documentation](docs/api.md) - Python API reference (if applicable)

## 🤝 Contributing

We love contributions! Whether it's:

- 🐛 Bug reports
- 💡 Feature suggestions
- 📖 Documentation improvements
- 🔧 Code contributions

Please check our [Contributing Guide](CONTRIBUTING.md) (coming soon) for details.

## 📄 License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.

The AGPL-3.0 ensures that any modifications to this CLI framework remain open source, benefiting the entire community.

## 🙏 Acknowledgments

### Built With

- [Click](https://click.palletsprojects.com/) - Command line interface creation kit
- [Black](https://github.com/psf/black) - The uncompromising code formatter
- [Ruff](https://github.com/astral-sh/ruff) - An extremely fast Python linter
- [MyPy](https://mypy-lang.org/) - Static type checker for Python
- [Rich](https://github.com/Textualize/rich) - Rich text and beautiful formatting

### Special Thanks

If you find ehAye™ Core CLI helpful, we'd appreciate a mention:

> This project was bootstrapped with [ehAye™ Core CLI](https://github.com/neekware/ehAyeCoreCLI)

## 🚦 Status

<div align="center">

**Project Status:** 🟢 Active Development

[![GitHub issues](https://img.shields.io/github/issues/neekware/ehAyeCoreCLI)](https://github.com/neekware/ehAyeCoreCLI/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/neekware/ehAyeCoreCLI)](https://github.com/neekware/ehAyeCoreCLI/pulls)
[![GitHub stars](https://img.shields.io/github/stars/neekware/ehAyeCoreCLI?style=social)](https://github.com/neekware/ehAyeCoreCLI)

</div>

---

<div align="center">

**Ready to build something amazing?**

[Get Started Now](#-quick-start) • [Star on GitHub](https://github.com/neekware/ehAyeCoreCLI) • [Report an Issue](https://github.com/neekware/ehAyeCoreCLI/issues)

<br>

Developed with ❤️ by [Val Neekman](https://github.com/un33k) @ [Neekware Inc.](https://neekware.com)

</div>