from types import MappingProxyType
from typing import Dict, Mapping

from pynalyzer.configuration_parsing.configuration import Configuration
from pynalyzer.configuration_parsing.configuration_parser import ConfigurationParser
from pynalyzer.configuration_parsing.configuration_path_finder import (
    ConfigurationPathFinder,
)
from pynalyzer.utils.converters import convert_path_collection_to_string


class CommandPreparer:
    @staticmethod
    def prepare_multiple(commands: Dict[str, str]) -> Mapping[str, str]:
        configuration_file_path = ConfigurationPathFinder.find()
        configuration = ConfigurationParser.parse(
            configuration_file_path=configuration_file_path,
        )
        filled_commands = CommandPreparer.__fill_commands(
            commands_to_fill=commands,
            configuration=configuration,
        )

        prepared_commands = MappingProxyType(filled_commands)
        return prepared_commands

    @staticmethod
    def __fill_commands(
        commands_to_fill: Dict[str, str],
        configuration: Configuration,
    ) -> Dict[str, str]:
        """
        Todo: Change to instance method for name mangling to work.
        """
        paths_to_analyze_str = convert_path_collection_to_string(
            path_collection=configuration.paths_to_analyze,
        )

        filled_commands = {}
        for command_alias, command_template in commands_to_fill.items():
            filled_template = command_template.format(
                config_file_path=configuration.config_file_path,
                paths_to_analyze=paths_to_analyze_str,
            )

            filled_commands[command_alias] = filled_template

        return filled_commands
