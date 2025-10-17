"""Main test file."""

from test_repo import foo


def test_foo() -> None:
    """Main Test."""
    assert foo("foo") == "foo"
