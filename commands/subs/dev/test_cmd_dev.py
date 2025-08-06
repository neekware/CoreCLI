#!/usr/bin/env python3
"""Tests for dev commands"""

import subprocess

import pytest


def run_cli_command(args: str) -> tuple[int, str, str]:
    """Run a CLI command and return exit code, stdout, stderr"""
    cmd = f"cli {args}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


class TestDevCommands:
    """Test suite for dev commands"""

    def test_dev_help(self) -> None:
        """Test that dev help works"""
        code, stdout, stderr = run_cli_command("dev --help")

        assert code == 0
        assert "Development tools" in stdout
        assert "format" in stdout
        assert "lint" in stdout
        assert "typecheck" in stdout
        assert "test" in stdout
        assert "precommit" in stdout

    def test_dev_format_help(self) -> None:
        """Test dev format help"""
        code, stdout, stderr = run_cli_command("dev format --help")

        assert code == 0
        assert "Format code with black" in stdout
        assert "--check" in stdout

    def test_dev_lint_help(self) -> None:
        """Test dev lint help"""
        code, stdout, stderr = run_cli_command("dev lint --help")

        assert code == 0
        assert "Lint code with ruff" in stdout
        assert "--fix" in stdout

    def test_dev_typecheck_help(self) -> None:
        """Test dev typecheck help"""
        code, stdout, stderr = run_cli_command("dev typecheck --help")

        assert code == 0
        assert "Type check with mypy" in stdout

    def test_dev_test_help(self) -> None:
        """Test dev test help"""
        code, stdout, stderr = run_cli_command("dev test --help")

        assert code == 0
        assert "Run pytest" in stdout

    def test_dev_precommit_help(self) -> None:
        """Test dev precommit help"""
        code, stdout, stderr = run_cli_command("dev precommit --help")

        assert code == 0
        assert "pre-commit checks" in stdout
        assert "--fix" in stdout

    def test_dev_completion_help(self) -> None:
        """Test dev completion help"""
        code, stdout, stderr = run_cli_command("dev completion --help")

        assert code == 0
        assert "Shell completion management" in stdout

    def test_dev_completion_test_help(self) -> None:
        """Test dev completion test help"""
        code, stdout, stderr = run_cli_command("dev completion test --help")

        assert code == 0
        assert "Test shell completion" in stdout

    def test_dev_completion_sync_help(self) -> None:
        """Test dev completion sync help"""
        code, stdout, stderr = run_cli_command("dev completion sync --help")

        assert code == 0
        assert "Sync shell completion" in stdout


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
