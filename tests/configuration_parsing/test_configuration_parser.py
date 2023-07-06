from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from pynalyzer.configuration_parsing.configuration import Configuration
from pynalyzer.configuration_parsing.configuration_parser import ConfigurationParser
from pynalyzer.utils.exceptions import (
    ConfigurationAttributeNotFoundError,
    ConfigurationSectionNotFoundError,
)


class TestConfigurationParser:
    __CONFIGURATION_FILE_PATH = Path("pyproject.toml")

    @patch.object(ConfigurationParser, "load_toml_data", return_value={"tool": {}})
    def test_parse_raises_configuration_section_not_found_error(
        self,
        _load_toml_data_mock: MagicMock,
    ) -> None:
        EXPECTED_ERROR_MESSAGE = (
            f"[tool.pynalyzer] section was not found in "
            f"{str(self.__CONFIGURATION_FILE_PATH)} configuration file"
        )

        with pytest.raises(
            expected_exception=ConfigurationSectionNotFoundError
        ) as exception_info:
            _ = ConfigurationParser.parse(
                configuration_file_path=self.__CONFIGURATION_FILE_PATH
            )

        assert str(exception_info.value) == EXPECTED_ERROR_MESSAGE

    @patch.object(
        ConfigurationParser, "load_toml_data", return_value={"tool": {"pynalyzer": ""}}
    )
    def test_parse_raises_configuration_attribute_not_found_error(
        self,
        _load_toml_data_mock: MagicMock,
    ) -> None:
        EXPECTED_ERROR_MESSAGE = (
            "paths attribute was not found under "
            "[tool.pynalyzer] section in configuration file"
        )

        with pytest.raises(
            expected_exception=ConfigurationAttributeNotFoundError
        ) as exception_info:
            _ = ConfigurationParser.parse(
                configuration_file_path=self.__CONFIGURATION_FILE_PATH
            )

        assert str(exception_info.value) == EXPECTED_ERROR_MESSAGE

    @patch.object(
        ConfigurationParser,
        "load_toml_data",
        return_value={"tool": {"pynalyzer": {"paths": ["src", "tests"]}}},
    )
    def test_parse_passes(
        self,
        _load_toml_data_mock: MagicMock,
    ) -> None:
        expected_parsed_configuration = Configuration(
            config_file_path=self.__CONFIGURATION_FILE_PATH,
            paths_to_analyze=(
                Path("src"),
                Path("tests"),
            ),
        )

        parsed_configuration = ConfigurationParser.parse(
            configuration_file_path=self.__CONFIGURATION_FILE_PATH
        )

        assert parsed_configuration == expected_parsed_configuration
