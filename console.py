"""
Developer Console

Copyright 2026 David Anthony Workman

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

See the LICENSE file in the project root for additional information.
"""
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
