import subprocess


def run_command(command, cwd=None):

    try:

        subprocess.run(
            command,
            cwd=cwd,
            check=True
        )

        return True

    except subprocess.CalledProcessError:

        print("\nCommand Failed")

        return False
