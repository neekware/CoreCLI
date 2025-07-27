# Shaypoor CLI

A clean, modular command-line interface demonstrating best practices in CLI development.

## Quick Start

```bash
# Setup (installs dependencies and pre-commit hooks)
./setup.sh

# Use the CLI
./cli --help
./cli proj -s              # Show repository size
./cli dev -a               # Run all code checks
```

## Features

- **Modular Architecture**: Each command group in its own module
- **Development Tools**: Integrated linting (ruff), formatting (black), and type checking (mypy)
- **Pre-commit Hooks**: Automatic code quality checks before commits
- **Auto-setup**: Virtual environment and dependencies managed automatically

## Project Structure

```
├── commandline/           # CLI implementation
│   ├── commands/         # Subcommand modules
│   │   ├── proj.py      # Project info commands
│   │   └── dev.py       # Development tools
│   └── main.py          # CLI entry point
├── setup.sh             # One-command setup
└── pyproject.toml       # Project configuration
```

## Development

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

## Architecture

See [commandline/README.md](commandline/README.md) for detailed architecture documentation.