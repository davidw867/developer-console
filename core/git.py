import subprocess
from core import state
from core.commands import run_command

def get_current_branch():
    """Return the name of the current Git branch."""

    if state.current_repository is None:
        return "None"

    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=state.current_repository,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except subprocess.CalledProcessError:
        return "Unknown"

def _check_repository():
    """Return False if no repository is selected."""
    if state.current_repository is None:
        print("\nNo repository selected.")
        return False
    return True


def git_status():
    """Show git status."""

    if not _check_repository():
        return

    run_command(
        ["git", "status"],
        cwd=state.current_repository
    )


def git_pull():
    """Pull the latest changes."""

    if not _check_repository():
        return

    run_command(
        ["git", "pull"],
        cwd=state.current_repository
    )


def git_push():
    """Push commits to the remote repository."""

    if not _check_repository():
        return

    run_command(
        ["git", "push"],
        cwd=state.current_repository
    )


def git_commit():
    """Create a commit."""

    if not _check_repository():
        return

    message = input("\nCommit Message: ").strip()

    if not message:
        print("Commit cancelled.")
        return

    if run_command(
        ["git", "add", "."],
        cwd=state.current_repository
    ):
        run_command(
            ["git", "commit", "-m", message],
            cwd=state.current_repository
        )


def quick_commit_push():
    """Add, commit, and push in one step."""

    if not _check_repository():
        return

    message = input("\nCommit Message: ").strip()

    if not message:
        print("Commit cancelled.")
        return

    if not run_command(
        ["git", "add", "."],
        cwd=state.current_repository
    ):
        return

    if not run_command(
        ["git", "commit", "-m", message],
        cwd=state.current_repository
    ):
        return

    run_command(
        ["git", "push"],
        cwd=state.current_repository
    )
