# Python Base Repository

Initial python project setup with Devcontainers, CI pipeline and the Serde library.

## Overview
This repository is based on [github.com/a5chin/python-uv](https://github.com/a5chin/python-uv). Check its readme for the main layout of this repository.

## TODO
- Improve documentation
- Add logging support

## Appendix

### Run Tests
```sh
uv run pytest
```

### Install Libraries
```sh
# Install also include develop dependencies
uv sync

# If you do not want dev dependencies to be installed
uv sync --no-dev

# Use the add command to add dependencies to your project
uv add {libraries}
```

## Run Command Line

```sh
uv run python src/main.py 42 Bob bob@example.com
uv run python src/main.py '{"id":42,"name":"Bob","email":"bob@example.com"}'
```
