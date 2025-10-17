"""Main test file."""

from test_repo import foo, main


def test_foo() -> None:
    """Test foo function."""
    assert foo("foo") == "foo"


def test_main(capsys) -> None:
    """Test main function."""
    main()
    captured = capsys.readouterr()
    assert "Hello from test-repo!" in captured.out
