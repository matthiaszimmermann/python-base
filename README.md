# Python Base Repository

A Python project template that emphasizes developer experience and code quality. 
This repository provides a consistent, containerized development environment with best-practice tooling pre-configured.

## Features

- **Dev Containers**: Consistent development environment across team members using VS Code and Docker
- **Modern Tooling**:
  - `uv`: Fast, reliable Python package management
  - `ruff`: All-in-one Python linter and formatter
  - `pyright`: Static type checking
  - `pytest`: Testing framework
- **Structured Logging**: Pre-configured JSON-based logging setup for structured, consistent log output
- **Type Safety**: Built-in support for Pydantic data validation and serialization
- **Quality Assurance**: Comprehensive linting, formatting, and testing pipeline

## Setup

1. Install [Docker](https://www.docker.com/get-started) and [VS Code](https://code.visualstudio.com/)
2. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension in VS Code
3. Clone this repository:
```bash
git clone https://github.com/matthiaszimmermann/python-base.git
```
4. Open the project in VS Code:
```bash
code python-base
```
5. When prompted, click "Reopen in Container"

## Development Workflow

### Code Quality Tools

The project uses `ruff` for both linting and formatting. Run the following command to check your code:
```bash
ruff check
```

### Testing

Run the test suite with:
```bash
pytest
```

### Logging

The project provides a centralized logging configuration through `logging_config.py` that:
- Loads structured logging settings from `logging_config.json`
- Ensures the configuration is loaded only once
- Provides a convenient `get_logger()` function for consistent logger creation

The JSON configuration includes:
- Structured logging with timestamp, logger name, level, and message
- Console output for development
- Configurable log levels (default: DEBUG for loggers, INFO for console output)
- Extensible format for adding custom handlers (e.g., file output, external services)

To use logging in your modules:
```python
from logging_config import get_logger

logger = get_logger(__name__)
logger.info("Application started")
```

## Example Usage

The repository includes example code demonstrating Pydantic model usage:
```sh
python src/main.py 42 Bob bob@example.com
python src/main.py '{"id":42,"name":"Bob","email":"bob@example.com"}'
```

## Contributing

This repository follows modern Python development practices. All configuration is centralized in `pyproject.toml` for maintainability. Before contributing:

1. Ensure your code passes all linting checks (`ruff check`)
2. Add tests for new functionality
3. Update documentation as needed
4. Verify all CI checks pass
