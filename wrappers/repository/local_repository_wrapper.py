from pathlib import Path
import shutil

from core.config import PROJECTS_DIR
from core import state

from core.commands import run_command
from core.config import PROJECTS_DIR
from core import state


def scan_repositories():
    """Return a list of all Git repositories in the Projects directory."""

    PROJECTS_DIR.mkdir(parents=True, exist_ok=True)

    repos = []

    for item in PROJECTS_DIR.iterdir():

        if item.is_dir() and (item / ".git").exists():
            repos.append(item)

    return sorted(repos, key=lambda repo: repo.name.lower())


def load_repositories():
    """Refresh the repository list."""

    state.repositories = scan_repositories()


def select_repository():
    """Allow the user to select the active repository."""

    load_repositories()

    if not state.repositories:
        print("\nNo repositories found.")
        return

    print("\nRepositories\n")

    for index, repo in enumerate(state.repositories, start=1):
        print(f"{index}. {repo.name}")

    choice = input("\nSelect Repository: ").strip()

    if not choice.isdigit():
        print("Invalid selection.")
        return

    choice = int(choice)

    if 1 <= choice <= len(state.repositories):
        state.current_repository = state.repositories[choice - 1]
        print(f"\nCurrent repository: {state.current_repository.name}")
    else:
        print("Invalid selection.")


def clone_repository():
    """Clone a Git repository into the Projects directory."""

    print("\nClone Repository")
    print("----------------")
    print("1. Compass")
    print("2. Portfolio")
    print("3. Custom URL")

    choice = input("\nChoice: ").strip()

    if choice == "1":
        repo_url = "git@github.com:davidw867/compass.git"

    elif choice == "2":
        repo_url = "git@github.com:davidw867/portfolio.git"

    elif choice == "3":
        repo_url = input("Repository URL: ").strip()

    else:
        print("Invalid choice.")
        return

    if run_command(
        ["git", "clone", repo_url],
        cwd=PROJECTS_DIR
    ):

        load_repositories()

        repo_name = repo_url.split("/")[-1].replace(".git", "")

        for repo in state.repositories:
            if repo.name == repo_name:
                state.current_repository = repo
                break

        print(f"\n'{repo_name}' cloned successfully.")


def delete_repository():
    """Delete the currently selected repository."""

    if state.current_repository is None:
        print("\nNo repository selected.")
        return

    print(f"\nDelete '{state.current_repository.name}'?")
    confirm = input("Type YES to confirm: ")

    if confirm != "YES":
        print("Cancelled.")
        return

    shutil.rmtree(state.current_repository)

    print("Repository deleted.")

    state.current_repository = None
    load_repositories()
