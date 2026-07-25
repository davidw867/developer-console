"""Application-wide constants for Developer Console.

This package contains fixed values that are not intended 
to change while the application is running.

User-configurable values do not belong here. They belong 
in the configuration layer.
"""

#------------------------------------------------------------------
# Application Constants
# ------------------------------------------------------------------
from core.constants.application import (
    APPLICATION_DESCRIPTION,
    APPLICATION_MODULE_NAME,
    APPLICATION_NAME,
    APPLICATION_PACKAGE_NAME,
    APPLICATION_VERSION,
    ARCHITECTURE_VERSION,
)

#------------------------------------------------------------------
# Console Constants
#------------------------------------------------------------------
from core.constants.console import (
    CONSOLE_NAME,
    CONSOLE_PROMPT,
    DEFAULT_ENCODING,
    EXIT_FAILURE,
    EXIT_SUCCESS,
)

#------------------------------------------------------------------
# Filesystem Constants
#------------------------------------------------------------------
from core.constants.filesystem import (
    APPLICATION_DIRECTORY,
    CACHE_DIRECTORY,
    CONFIG_DIRECTORY,
    LOG_DIRECTORY,
    TEMP_DIRECTORY,
    CONFIG_FILE_NAME,
    LOG_FILE_NAME,
    HISTORY_FILE_NAME,
    JSON_EXTENSION,
    TOML_EXTENSION,
    YAML_EXTENSION,
    LOG_EXTENSION,
    USER_HOME_DIRECTORY,
)

#------------------------------------------------------------------
# Environment Constants
#------------------------------------------------------------------
from core.constants.environment import (
    HOME_ENVIRONMENT_VARIABLE,
    PATH_ENVIRONMENT_VARIABLE,
    SHELL_ENVIRONMENT_VARIABLE,
    TERM_ENVIRONMENT_VARIABLE,
    TMP_ENVIRONMENT_VARIABLE,
    USER_ENVIRONMENT_VARIABLE,
    TEMP_ENVIRONMENT_VARIABLE,
    LANG_ENVIRONMENT_VARIABLE,
    HOSTNAME_ENVIRONMENT_VARIABLE,
)

__all__: list[str] = [
#------------------------------------------------------------------
# Application Constants
#------------------------------------------------------------------
    "APPLICATION_DESCRIPTION",
    "APPLICATION_MODULE_NAME",
    "APPLICATION_NAME",
    "APPLICATION_PACKAGE_NAME",
    "APPLICATION_VERSION",
    "ARCHITECTURE_VERSION",

#------------------------------------------------------------------
# Console Constants
#------------------------------------------------------------------
    "CONSOLE_NAME",
    "CONSOLE_PROMPT",
    "DEFAULT_ENCODING",
    "EXIT_SUCCESS",
    "EXIT_FAILURE",

#------------------------------------------------------------------
# Filesystem Constants
#------------------------------------------------------------------
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

#------------------------------------------------------------------
# Environmemt Constants
#------------------------------------------------------------------
    "HOME_ENVIRONMENT_VARIABLE",
    "PATH_ENVIRONMENT_VARIABLE",
    "SHELL_ENVIRONMENT_VARIABLE",
    "TERM_ENVIRONMENT_VARIABLE",
    "TMP_ENVIRONMENT_VARIABLE",
    "USER_ENVIRONMENT_VARIABLE",
    "TEMP_ENVIRONMENT_VARIABLE",
    "LANG_ENVIRONMENT_VARIABLE",
    "HOSTNAME_ENVIRONMENT_VARIABLE",
]
