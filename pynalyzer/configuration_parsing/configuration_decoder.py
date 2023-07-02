from pathlib import Path
from typing import Any, Dict

from pynalyzer.configuration_parsing.configuration import Configuration
from pynalyzer.utils.exceptions import ConfigurationAttributeNotFoundError


class ConfigurationDecoder:
    @staticmethod
    def decode(
        configuration_file_path: Path,
        configuration_data: Dict[str, Any],
    ) -> Configuration:
        """
        Todo:
            - Use more sophisticated decoding with validation
                of fields using pydantic or dacite.
            - Add KeyError handling for ["paths"]
        """
        ConfigurationDecoder.__validate_configuration(
            configuration_data=configuration_data
        )

        decoded_configuration = Configuration(
            config_file_path=configuration_file_path,
            paths_to_analyze=tuple(Path(path) for path in configuration_data["paths"]),
        )

        return decoded_configuration

    @staticmethod
    def __validate_configuration(configuration_data: Dict[str, Any]) -> None:
        ATTRIBUTES_TO_CHECK = ("paths",)

        for attribute in ATTRIBUTES_TO_CHECK:
            if attribute not in configuration_data:
                raise ConfigurationAttributeNotFoundError(attribute_name=attribute)
