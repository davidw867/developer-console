import subprocess
from core import state
from core.git import get_current_branch

def clear():
    subprocess.run(["clear"])


def pause():
    input("\nPress Enter...")


def header():

    print("=" * 40)
    print("Developer Console v0.3.1")
    print("=" * 40)

    if state.current_repository:

        print(f"Repository : {state.current_repository.name}")
        print(f"Branch     : {get_current_branch()}")

    else:

        print("Repository : None")
        print("Branch     : None")

    print("=" * 40)
