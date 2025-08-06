# Testing Guide for ehAye™ Core CLI

## 🧪 Testing Options

### 1. Local Testing (Quick)

```bash
# Run all checks locally
source .venv/bin/activate
cli dev all
```

### 2. Docker Testing (Simulates CI)

```bash
# Quick test with default Python version
./test-docker.sh quick

# Test with all Python versions
./test-docker.sh full

# Test with specific Python version
./test-docker.sh single 3.9

# Interactive shell in test container
./test-docker.sh shell
```

### 3. GitHub Actions Testing with Act

```bash
# Install act (one-time setup)
brew install act  # macOS
# or
curl https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash  # Linux

# Test GitHub Actions locally
./test-with-act.sh

# Test specific workflow
act push --workflows .github/workflows/test.yml

# Test with specific Python version
act push --matrix python-version:3.9

# List what would run
act -l
```

### 4. Docker Compose Testing

```bash
# Run quick test
docker-compose -f docker-compose.test.yml run --rm quick-test

# Test specific Python version
docker-compose -f docker-compose.test.yml run --rm test-py39
docker-compose -f docker-compose.test.yml run --rm test-py311

# Run all tests
docker-compose -f docker-compose.test.yml up
```

## 🐛 Troubleshooting

### Module Import Errors

If you see `ModuleNotFoundError: No module named 'commands.subs'`:

1. **When running from source:**
   ```bash
   export PYTHONPATH="${PYTHONPATH}:$(pwd)"
   python -m commands --version
   ```

2. **When installed:**
   ```bash
   pip install -e .
   cli --version
   ```

### Docker Issues

1. **Docker not running:**
   - Start Docker Desktop
   - Check: `docker info`

2. **Permission denied:**
   ```bash
   sudo usermod -aG docker $USER
   # Log out and back in
   ```

3. **Build cache issues:**
   ```bash
   docker-compose -f docker-compose.test.yml build --no-cache
   ```

### GitHub Actions Issues

1. **Act not working:**
   - Make sure Docker is running
   - Try: `act -v` for verbose output
   - Use: `--container-architecture linux/amd64` on M1 Macs

2. **Workflow syntax errors:**
   ```bash
   # Validate workflow files
   act -n  # Dry run
   ```

## 📊 Test Coverage

Run tests with coverage:

```bash
# Local coverage
pytest --cov=commands --cov-report=html
open htmlcov/index.html

# In Docker
docker run --rm -v $(pwd):/app ehaye-cli-test:latest \
  pytest --cov=commands --cov-report=html
```

## 🔄 Continuous Integration

The project has two CI workflows:

1. **test.yml** - Quick tests on push/PR
2. **ci.yml** - Comprehensive testing matrix

### Testing Matrix

- **Operating Systems:** Ubuntu, macOS, Windows
- **Python Versions:** 3.9, 3.10, 3.11, 3.12, 3.13
- **Test Types:** Unit, Integration, Installation, CLI

## 📝 Writing Tests

Add new tests to `commands/tests/`:

```python
# commands/tests/test_new_feature.py
import pytest
from click.testing import CliRunner
from commands.main import cli

def test_new_command():
    runner = CliRunner()
    result = runner.invoke(cli, ['new-command'])
    assert result.exit_code == 0
    assert 'expected output' in result.output
```

## 🚀 Pre-commit Hooks

Before committing:

```bash
# Run pre-commit manually
cli dev precommit --fix

# Install hooks (one-time)
pre-commit install

# Skip hooks if needed
git commit --no-verify
```

## 📦 Testing Installation

```bash
# Test pip installation
python -m venv test-env
source test-env/bin/activate
pip install .
cli --version
deactivate
rm -rf test-env

# Test editable installation
pip install -e .
cli --version

# Test from PyPI (when published)
pip install core-cli
cli --version
```