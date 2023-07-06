from typing import Dict

from pynalyzer.commands_handling.command_preparer import CommandPreparer
from pynalyzer.commands_handling.command_runner import CommandRunner


class CommandExecutor:
    @staticmethod
    def execute_multiple(commands: Dict[str, str]) -> None:
        prepared_commands = CommandPreparer.prepare_multiple(commands=commands)
        CommandRunner.run_multiple(prepared_commands=prepared_commands)
