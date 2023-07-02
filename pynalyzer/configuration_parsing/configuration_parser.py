import sys
from typing import Any, Dict

from pynalyzer.utils.exceptions import ConfigurationSectionNotFoundError

if sys.version_info >= (3, 11):
    import tomllib as tomli
else:
    import tomli

from pathlib import Path

from pynalyzer.configuration_parsing.configuration import Configuration
from pynalyzer.configuration_parsing.configuration_decoder import ConfigurationDecoder


class ConfigurationParser:
    @staticmethod
    def parse(configuration_file_path: Path) -> Configuration:
        data = ConfigurationParser.load_toml_data(
            toml_file_path=configuration_file_path
        )

        try:
            configuration_data = data["tool"]["pynalyzer"]
        except KeyError:
            raise ConfigurationSectionNotFoundError(
                configuration_file_path=configuration_file_path
            )

        parsed_configuration = ConfigurationDecoder.decode(
            configuration_file_path=configuration_file_path,
            configuration_data=configuration_data,
        )

        return parsed_configuration

    @staticmethod
    def load_toml_data(toml_file_path: Path) -> Dict[str, Any]:
        with open(toml_file_path, mode="rb") as toml_file:
            data = tomli.load(toml_file)

        return data
