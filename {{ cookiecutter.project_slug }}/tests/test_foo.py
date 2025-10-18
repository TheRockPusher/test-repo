"""Main test file."""

from {{ cookiecutter.package_slug }} import foo, main


def test_foo() -> None:
    """Test foo function."""
    assert foo("foo") == "foo"


def test_main(capsys) -> None:
    """Test main function."""
    main()
    captured = capsys.readouterr()
    assert "Hello from {{ cookiecutter.project_name }}!" in captured.out
