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

# ====================≠=================≠===≠=============================
# Exit Code Constants
# ≠=======================================================================
from core.constants.exit_code.py import (

    # =========================================================================
    # POSIX Exit Codes
    # =========================================================================
    EXIT_SUCCESS_CODE,
    EXIT_FAILURE_CODE,
    EXIT_USAGE_ERROR_CODE,
    EXIT_CANNOT_EXECUTE_CODE,
    EXIT_COMMAND_NOT_FOUND_CODE,
    EXIT_INTERRUPTED_CODE,
    EXIT_TERMINATED_CODE,

    # =========================================================================
    # Subprocess Exit Codes
    # =========================================================================
    EXIT_INVALID_EXIT_ARGUMENT_CODE,
    EXIT_OUT_OF_RANGE_CODE,

    # =========================================================================
    # Developer Console Exit Codes
    # =========================================================================
    EXIT_CONFIGURATION_ERROR_CODE,
    EXIT_VALIDATION_ERROR_CODE,
    EXIT_INITIALIZATION_ERROR_CODE,
    EXIT_PERMISSION_DENIED_CODE,
    EXIT_NETWORK_ERROR_CODE,
    EXIT_TIMEOUT_ERROR_CODE,
    EXIT_DEPENDENCY_ERROR_CODE,
    EXIT_CACHE_ERROR_CODE,
    EXIT_GITHUB_ERROR_CODE,
    EXIT_NOT_IMPLEMENTED_ERROR_CODE,
)

# ==========≠=================================================================
# Git Constants 
# ======≠=====================================================================
from core.constants.git.py import (

    # =============================================>
    # Git Executable
    # =============================================>
    GIT_COMMAND,

    # =============================================>
    # Git Commands
    # =============================================>
    GIT_CLONE_COMMAND,
    GIT_STATUS_COMMAND,
    GIT_ADD_COMMAND,
    GIT_COMMIT_COMMAND,
    GIT_PUSH_COMMAND,
    GIT_PULL_COMMAND,
    GIT_FETCH_COMMAND,
    GIT_BRANCH_COMMAND,
    GIT_REMOTE_COMMAND,
    GIT_CONFIG_COMMAND,
    GIT_REV_PARSE_COMMAND,

    # =============================================>
    # Git Flags
    # =============================================>
    GIT_VERSION_FLAG,
    GIT_MESSAGE_FLAG,
    GIT_PORCELAIN_FLAG,

    # =============================================>
    # Git Repository
    # =============================================>
    GIT_DEFAULT_REMOTE_NAME,
    GIT_DIRECTORY_NAME,
    GIT_IGNORE_FILE_NAME,
)

# ==================================================
# GitHub Constants
# =================================================
from core.constants.github.py import (

      #=======≠=====================================>
      # Github CLI
      # =============================================>
      GITHUB_COMMAND,

      # ======≠======================================>
      # Authentication
      # =============================================>
      GITHUB_AUTH_COMMAND,
      GITHUB_LOGIN_COMMAND,
      GITHUB_STATUS_COMMAND,

      # =============================================>
      # Repository
      # =============================================>
      GITHUB_REPOSITORY_COMMAND,
      GITHUB_CLONE_COMMAND,

      # =============================================>
      # API
      # =============================================>
      GITHUB_API_COMMAND,

      # =============================================>
      # Global Flags
      # =============================================>
      GITHUB_VERSION_FLAG,
      GITHUB_REPOSITORY_FLAG,
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

    # =========================================================================
    # POSIX Exit Codes Constants
    # =========================================================================
    "EXIT_SUCCESS_CODE",
    "EXIT_FAILURE_CODE",
    "EXIT_USAGE_ERROR_CODE",
    "EXIT_CANNOT_EXECUTE_CODE",
    "EXIT_COMMAND_NOT_FOUND_CODE",
    "EXIT_INTERRUPTED_CODE",
    "EXIT_TERMINATED_CODE",

    # =========================================================================
    # Subprocess Exit Codes Constants
    # =========================================================================
    "EXIT_INVALID_EXIT_ARGUMENT_CODE",
    "EXIT_OUT_OF_RANGE_CODE",

    # =========================================================================
    # Developer Console Exit Codes Constants
    # =========================================================================
    "EXIT_CONFIGURATION_ERROR_CODE",
    "EXIT_VALIDATION_ERROR_CODE",
    "EXIT_INITIALIZATION_ERROR_CODE",
    "EXIT_PERMISSION_DENIED_CODE",
    "EXIT_NETWORK_ERROR_CODE",
    "EXIT_TIMEOUT,_ERROR_CODE",
    "EXIT_DEPENDENCY_ERROR_CODE",
    "EXIT_CACHE_ERROR_CODE",
    "EXIT_GITHUB_ERROR_CODE",
    "EXIT_NOT_IMPLEMENTED_ERROR_CODE",

    # =========================================>
    # Git Executable
    # =========================================>
    "GIT_COMMAND",

    # =========================================>
    # Git Commands
    # =========================================>
    "GIT_CLONE_COMMAND",
    "GIT_STATUS_COMMAND",
    "GIT_ADD_COMMAND",
    "GIT_COMMIT_COMMAND",
    "GIT_PUSH_COMMAND",
    "GIT_PULL_COMMAND",
    "GIT_FETCH_COMMAND",
    "GIT_BRANCH_COMMAND",
    "GIT_REMOTE_COMMAND",
    "GIT_CONFIG_COMMAND",
    "GIT_REV_PARSE_COMMAND",

    # =========================================>
    # Git Flags
    # =========================================>
    "GIT_VERSION_FLAG",
    "GIT_MESSAGE_FLAG",
    "GIT_PORCELAIN_FLAG",

    # =========================================>
    # Git Repository
    # =========================================>
    "GIT_DEFAULT_REMOTE_NAME",
    "GIT_DIRECTORY_NAME",
    "GIT_IGNORE_FILE_NAME",

    #=======≠================================>
    # Github CLI
    # =======================================>
    "GITHUB_COMMAND",

    # ======≠================================>
    # Authentication
    # =======================================>
    "GITHUB_AUTH_COMMAND",
    "GITHUB_LOGIN_COMMAND",
    "GITHUB_STATUS_COMMAND",

    # =======================================>
    # Repository
    # =======================================>
    "GITHUB_REPOSITORY_COMMAND",
    "GITHUB_CLONE_COMMAND",

    # =======================================>
    # API
    # =======================================>
    "GITHUB_API_COMMAND",

    # =======================================>
    # Global Flags
    # =======================================>
    "GITHUB_VERSION_FLAG",
    "GITHUB_REPOSITORY_FLAG",

]
