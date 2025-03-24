# Pyton Base Repository

Initial Python project setup with Devcontainers, CI pipeline and the Pydantic library.

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

## TODO

- remove .vscode folder (move to .devcontainer/devcontainer.json)
- streamline gihub setup/pipelines
- add user test

## Usage
Once the dev container is built and running, you can use the integrated terminal in VS Code to run commands.

### Formatting
```bash
ruff check
```

### Running Tests
To run all tests:
```bash
pytest
```

## Run Example
```sh
python src/main.py 42 Bob bob@example.com
python src/main.py '{"id":42,"name":"Bob","email":"bob@example.com"}'
```
