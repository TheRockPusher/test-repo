# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Features

- Modern Python packaging layout with `src/` modules.
- Type hints shipped via `py.typed` markers.
- Ready-to-use linting, formatting, testing, and coverage tooling.

## Getting started

Create your environment and install the project dependencies with [uv](https://docs.astral.sh/uv/):

```bash
make install
```

Run the test suite to validate everything is wired correctly:

```bash
make test
```

Additional commands are documented in the `Makefile`. Use `make help` to see the full list.

## Project metadata

- **Author:** {{ cookiecutter.author_name }} (<{{ cookiecutter.author_email }}>)
- **Homepage:** {{ cookiecutter.github_url }}
- **License:** {% if cookiecutter.license == 'MIT' %}MIT License{% elif cookiecutter.license == 'GPL-3.0-only' %}GNU General Public License v3.0 only{% else %}GNU Affero General Public License v3.0 only{% endif %}

## License

This project is licensed under the terms of the {% if cookiecutter.license == 'MIT' %}MIT License{% elif cookiecutter.license == 'GPL-3.0-only' %}GNU General Public License v3.0 only{% else %}GNU Affero General Public License v3.0 only{% endif %}. See the [LICENSE](LICENSE) file for the full text.
