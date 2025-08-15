# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

### Using uv (recommended)

```bash
uv add {{ cookiecutter.package_slug }}
```

### Using pip

```bash
pip install {{ cookiecutter.package_slug }}
```

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and development workflows.

### Setup

1. Clone the repository:
   ```bash
   git clone {{ cookiecutter.repository_url }}
   cd {{ cookiecutter.package_slug }}
   ```

2. Install dependencies:
   ```bash
   uv sync --dev
   ```

### Development Tools

This project includes optional development tools:

{% if cookiecutter.use_black == "y" %}
#### Code Formatting with Black
```bash
uv run black src/ tests/
```
{% endif %}

{% if cookiecutter.use_isort == "y" %}
#### Import Sorting with isort
```bash
uv run isort src/ tests/
```
{% endif %}

{% if cookiecutter.use_flake8 == "y" %}
#### Linting with flake8
```bash
uv run flake8 src/ tests/
```
{% endif %}

{% if cookiecutter.use_mypy == "y" %}
#### Type Checking with mypy
```bash
uv run mypy src/
```
{% endif %}

{% if cookiecutter.use_pytest == "y" %}
#### Testing with pytest
```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Run tests in watch mode
uv run pytest --watch
```
{% endif %}

### Building

Build the package:
```bash
uv build
```

## Usage

```python
from {{ cookiecutter.package_slug }} import hello

# Basic usage
print(hello())  # Hello, World!

# With custom name
print(hello("Alice"))  # Hello, Alice!
```

## License

This project is licensed under the {{ cookiecutter.license }} License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Authors

* **{{ cookiecutter.author_name }}** - *Initial work* - [{{ cookiecutter.github_username }}](https://github.com/{{ cookiecutter.github_username }})