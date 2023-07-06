from pynalyzer.commands_handling.command_executor import CommandExecutor


class Entrypoint:
    @staticmethod
    def check() -> None:
        check_commands = {
            "isort": "isort --check-only --diff --settings-path {config_file_path} {paths_to_analyze}",
            "black": "black --diff --check --config {config_file_path} {paths_to_analyze}",
            "mypy": "mypy --config-file {config_file_path} {paths_to_analyze}",
            "bandit": "bandit -c {config_file_path} -r {paths_to_analyze}",
        }

        CommandExecutor.execute_multiple(commands=check_commands)

    @staticmethod
    def fix() -> None:
        fix_commands = {
            "isort": "isort --settings-path {config_file_path} {paths_to_analyze}",
            "black": "black --config {config_file_path} {paths_to_analyze}",
        }

        CommandExecutor.execute_multiple(commands=fix_commands)
