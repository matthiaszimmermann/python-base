import json
from logging import Logger, config, getLogger
from pathlib import Path

LOGGER_CONFIG_FILE = Path("logging_config.json")

logger_config_loaded = False


def setup_logging() -> None:  # noqa: D103
    global logger_config_loaded  # noqa: PLW0603

    if logger_config_loaded:
        return

    with Path("logging_config.json").open() as f:
        config_from_json = json.load(f)

    config.dictConfig(config_from_json)
    logger_config_loaded = True


def get_logger(name: str) -> Logger:  # noqa: D103
    setup_logging()
    return getLogger(name)
