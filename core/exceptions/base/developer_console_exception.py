
"""Base exception for Developer Console errors."""

from typing import Optional


class DeveloperConsoleException(Exception):
    """Base exception for all Developer Console-specific errors."""

    def __init__(
        self,
        message: str,
        original_exception: Optional[BaseException] = None,
    ) -> None:
        super().__init__(message)

        self.message = message
        self.original_exception = original_exception
