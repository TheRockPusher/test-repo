"""Test repository package."""


def foo(value: str) -> str:
    """Return the input value unchanged.

    Args:
        value: The input string to return.

    Returns:
        The same string that was passed in.

    """
    return value


def main() -> None:
    """Print a greeting message."""
    print("Hello from test-repo!")  # noqa: T201
