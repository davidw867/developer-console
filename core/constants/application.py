"""Fixed application identity constants for Developer Console."""

APPLICATION_NAME: str = "Developer Console"
APPLICATION_PACKAGE_NAME: str = "developer-console"
APPLICATION_MODULE_NAME: str = "developer_console"

APPLICATION_VERSION: str = "0.1.0"
ARCHITECTURE_VERSION: str = "1.0"

APPLICATION_DESCRIPTION: str = (
    "A lightweight, Termux-first developer automation framework."
)

__all__: list[str] = [
    "APPLICATION_NAME",
    "APPLICATION_PACKAGE_NAME",
    "APPLICATION_MODULE_NAME",
    "APPLICATION_VERSION",
    "ARCHITECTURE_VERSION",
    "APPLICATION_DESCRIPTION",
]
