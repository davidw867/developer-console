"""Filesystem-related constants for Developer Console."""

from pathlib import Path

# ---------------------------------------------------------------------------
# Hidden Application Directories
# ---------------------------------------------------------------------------

APPLICATION_DIRECTORY: str = ".developer_console"
CACHE_DIRECTORY: str = "cache"
CONFIG_DIRECTORY: str = "config"
LOG_DIRECTORY: str = "logs"
TEMP_DIRECTORY: str = "temp"

# ---------------------------------------------------------------------------
# Common File Names
# ---------------------------------------------------------------------------

CONFIG_FILE_NAME: str = "config.toml"
LOG_FILE_NAME: str = "developer-console.log"
HISTORY_FILE_NAME: str = "history.log"

# ---------------------------------------------------------------------------
# File Extensions
# ---------------------------------------------------------------------------

JSON_EXTENSION: str = ".json"
TOML_EXTENSION: str = ".toml"
YAML_EXTENSION: str = ".yaml"
LOG_EXTENSION: str = ".log"

# ---------------------------------------------------------------------------
# User Home Directory
# ---------------------------------------------------------------------------

USER_HOME_DIRECTORY: Path = Path.home()

__all__: list[str] = [
    "APPLICATION_DIRECTORY",
    "CACHE_DIRECTORY",
    "CONFIG_DIRECTORY",
    "LOG_DIRECTORY",
    "TEMP_DIRECTORY",
    "CONFIG_FILE_NAME",
    "LOG_FILE_NAME",
    "HISTORY_FILE_NAME",
    "JSON_EXTENSION",
    "TOML_EXTENSION",
    "YAML_EXTENSION",
    "LOG_EXTENSION",
    "USER_HOME_DIRECTORY",
]
