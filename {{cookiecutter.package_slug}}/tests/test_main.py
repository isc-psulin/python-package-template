{% if cookiecutter.use_pytest == "y" %}"""Tests for the main module."""

import pytest

from {{ cookiecutter.package_slug }}.main import hello


def test_hello_default():
    """Test hello function with default parameter."""
    result = hello()
    assert result == "Hello, World!"


def test_hello_with_name():
    """Test hello function with custom name."""
    result = hello("Alice")
    assert result == "Hello, Alice!"


@pytest.mark.parametrize("name,expected", [
    ("Bob", "Hello, Bob!"),
    ("Charlie", "Hello, Charlie!"),
    ("", "Hello, !"),
])
def test_hello_parametrized(name, expected):
    """Test hello function with various names."""
    assert hello(name) == expected
{% endif %}