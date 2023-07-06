import subprocess  # nosec B404
from typing import Mapping


class CommandRunner:
    @staticmethod
    def run_multiple(prepared_commands: Mapping[str, str]) -> None:
        for cmd_alias, command in prepared_commands.items():
            CommandRunner.run(command=command)

    @staticmethod
    def run(command: str) -> None:
        subprocess.run(
            args=command.split(" "),
            check=True,
            shell=False,  # nosec B603
        )
