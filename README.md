# Python Dev Container Repository

## Overview
This repository is based on [github.com/a5chin/python-uv](https://github.com/a5chin/python-uv). Check its readme for the main layout of this repository.

## TODO
- Improve documentation
- Add logging support

## Appendix

### Run Tests
```sh
pytest
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
