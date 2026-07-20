from core.console import clear, header, pause
from core.state import RepositoryState, ConsoleState

from core.github import (
    is_authenticated,
    login,
    create_repository,
    clone_repository,
    delete_repository,
    list_repositories
)

from core.local_repositories import (
    load_repositories,
    select_repository,
    delete_repository,
    clone_repository,
)

from core.git import (
    git_status,
    git_pull,
    git_commit,
    git_push,
    get_repository_state,
    quick_commit_push)


def main():
    print(get_repository_state())
    load_repositories()

    while True:

        clear()

        header()

        print("""
1. Select Repository

Git
---
2. Status
3. Pull
4. Commit
5. Push
6. Quick Commit & Push

Repositories
------------
7. Clone Repository
8. Delete Repository
9. Refresh

0. Exit
""")

        choice = input("Choice: ")

        match choice:

            case "1":
                select_repository()

            case "2":
                git_status()

            case "3":
                git_pull()

            case "4":
                git_commit()

            case "5":
                git_push()

            case "6":
                quick_commit_push()

            case "7":
                clone_repository()

            case "8":
                delete_repository()

            case "9":
                load_repositories()

            case "0":
                break

            case _:
                print("Invalid Choice")

        pause()


if __name__ == "__main__":
    main()
