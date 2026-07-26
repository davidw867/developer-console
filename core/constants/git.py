# ============================================================================
# Git Executable
# ============================================================================
GIT_COMMAND: str = "git"

# ============================================================================
# Git Commands
# ============================================================================
GIT_CLONE_COMMAND: str = "clone"
GIT_STATUS_COMMAND: str = "status"
GIT_ADD_COMMAND: str = "add"
GIT_COMMIT_COMMAND: str = "commit"
GIT_PUSH_COMMAND: str = "push"
GIT_PULL_COMMAND: str = "pull"
GIT_FETCH_COMMAND: str = "fetch"
GIT_BRANCH_COMMAND: str = "branch"
GIT_REMOTE_COMMAND: str = "remote"
GIT_CONFIG_COMMAND: str = "config"
GIT_REV_PARSE_COMMAND: str = "rev-parse"

# ============================================================================
# Git Flags
# ============================================================================
GIT_VERSION_FLAG: str = "--version"
GIT_MESSAGE_FLAG: str = "--message"
GIT_PORCELAIN_FLAG: str = "--porcelain"

# ============================================================================
# Git Repository
# ============================================================================
GIT_DEFAULT_REMOTE_NAME: str = "origin"
GIT_DIRECTORY_NAME: str = ".git"
GIT_IGNORE_FILE_NAME: str = ".gitignore"

__all__: list[str] = [
    # ≠=======================================================
    # Git Executable
    # ========================================================
    "GIT_COMMAND",

    # ========================================================
    # Git Commands
    # ========================================================
    "GIT_CLONE_COMMAND",
    "GIT_STATUS_COMMAND",
    "GIT_ADD_COMMAND",
    "GIT_COMMIT_COMMAND"
    "GIT_PUSH_COMMAND",
    "GIT_PULL_COMMAND",
    "GIT_FETCH_COMMAND",
    "GIT_BRANCH_COMMAND",
    "GIT_REMOTE_COMMAND",
    "GIT_CONFIG_COMMAND",

    # ≠=======================================================
    # Git Flags
    # ========================================================
    "GIT_VERSION_FLAG",
    "GIT_MESSAGE_FLAG",
    "GIT_PORCELAIN_FLAG",

    # ≠=======================================================
    # Git Repository
    # ========================================================
    "GIT_DEFAULT_REMOTE_NAME",
    "GIT_DIRECTORY_NAME",
    "GIT_IGNORE_FILE_NAME",
]
