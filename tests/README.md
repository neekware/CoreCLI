# Tests Directory Structure

This directory contains all test-related files organized by functionality.

## Directory Structure

```
tests/
├── commands/      # Unit tests for CLI commands (moved from commands/tests/)
├── docker/        # Docker-related test configurations
├── env/           # Test environment setups and fixtures
├── integration/   # Integration tests
├── rust/          # Rust-related tests (when applicable)
└── e2e/           # End-to-end tests (future)
```

## Test Categories

### commands/
Unit tests for all CLI commands. These test individual command functionality in isolation.

### docker/
Contains Docker Compose files and Dockerfiles for testing the application in containerized environments.

### env/
Test environment configurations, fixtures, and temporary test data. Virtual environments for testing should be created here.

### integration/
Integration tests that test multiple components working together.

### rust/ (future)
Tests for Rust components when building mixed-language projects.

## Running Tests

```bash
# Run all tests
cli dev test

# Run with coverage
pytest --cov=commands

# Run specific test category
pytest tests/commands/
pytest tests/integration/
```

## Test Conventions

1. **Naming**: Test files should be named `test_*.py`
2. **Structure**: Mirror the source code structure within each test category
3. **Isolation**: Each test should be independent and not rely on other tests
4. **Cleanup**: Tests should clean up any temporary files or directories they create
5. **Documentation**: Complex tests should include docstrings explaining what they test

## Temporary Files

Any temporary files or directories created during testing should be placed in `tests/env/tmp/` and cleaned up after the test completes.