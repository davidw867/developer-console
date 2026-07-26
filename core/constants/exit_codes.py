""" Consts Exit Codes for Standard POSIX, SUBOROCCES, DEVELOPER CONSOLE. """

# ============================================================================
# Standard POSIX Exit Codes
# ============================================================================
EXIT_SUCCESS_CODE: int = 0
EXIT_FAILURE_CODE: int = 1
EXIT_USAGE_ERROR_CODE: int = 2
EXIT_CANNOT_EXECUTE_CODE: int = 126
EXIT_COMMAND_NOT_FOUND_CODE: int = 127
EXIT_INTERRUPTED_CODE: int = 130      # Ctrl+C
EXIT_TERMINATED_CODE: int = 143       # SIGTERM

# ============================================================================
# Subprocces Exit Codes
# ============================================================================
EXIT_INVALID_EXIT_ARGUMENT_CODE: int = 128
EXIT_OUT_OF_RANGE_CODE: int = 255

# ============================================================================
# Developer Console Exit Codes
# ============================================================================
EXIT_CONFIGURATION_ERROR_CODE: int = 100
EXIT_VALIDATION_ERROR_CODE: int = 101
EXIT_INITIALIZATION_ERROR_CODE: int = 102
EXIT_PERMISSION_DENIED_CODE: int = 103
EXIT_NETWORK_ERROR_CODE: int = 104
EXIT_TIMEOUT_CODE: int = 105
EXIT_DEPENDENCY_ERROR_CODE: int = 106
EXIT_CACHE_ERROR_CODE: int = 107
EXIT_GITHUB_ERROR_CODE: int = 108
EXIT_NOT_IMPLEMENTED_CODE: int = 109

__all__: list[str] = [

    # =========================================================================
    # POSIX Exit Codes
    # =========================================================================

    "EXIT_SUCCESS_CODE",
    "EXIT_FAILURE_CODE",
    "EXIT_USAGE_ERROR_CODE",
    "EXIT_CANNOT_EXECUTE_CODE",
    "EXIT_COMMAND_NOT_FOUND_CODE",
    "EXIT_INTERRUPTED_CODE",
    "EXIT_TERMINATED_CODE",

    # =========================================================================
    # Subprocess Exit Codes
    # =========================================================================
    "EXIT_INVALID_EXIT_ARGUMENT_CODE",
    "EXIT_OUT_OF_RANGE_CODE",

    # =========================================================================
    # Developer Console Exit Codes
    # =========================================================================
    "EXIT_CONFIGURATION_ERROR_CODE",
    "EXIT_VALIDATION_ERROR_CODE",
    "EXIT_INITIALIZATION_ERROR_CODE",
    "EXIT_PERMISSION_DENIED_CODE",
    "EXIT_NETWORK_ERROR_CODE",
    "EXIT_TIMEOUT_ERROR_CODE",
    "EXIT_DEPENDENCY_ERROR_CODE",
    "EXIT_CACHE_ERROR_CODE",
    "EXIT_GITHUB_ERROR_CODE",
    "EXIT_NOT_IMPLEMENTED_ERROR_CODE",

]
