from pathlib import Path
from types import MappingProxyType
from typing import Dict, Mapping
from unittest.mock import MagicMock, patch

import pytest

from pynalyzer.commands_handling.command_preparer import CommandPreparer
from pynalyzer.configuration_parsing.configuration import Configuration
from pynalyzer.configuration_parsing.configuration_parser import ConfigurationParser
from pynalyzer.configuration_parsing.configuration_path_finder import (
    ConfigurationPathFinder,
)


class TestCommandPreparer:
    @pytest.mark.parametrize(
        "commands, configuration, expected_result",
        [
            (
                {
                    "isort": "isort --settings-path {config_file_path} {paths_to_analyze}",
                },
                Configuration(
                    config_file_path=Path("pyproject.toml"),
                    paths_to_analyze=(
                        Path("src"),
                        Path("tests"),
                    ),
                ),
                MappingProxyType(
                    {
                        "isort": "isort --settings-path pyproject.toml src tests",
                    }
                ),
            ),
        ],
    )
    @patch.object(ConfigurationPathFinder, "find")
    def test_prepare_multiple_passes(
        self,
        _find_mock: MagicMock,
        commands: Dict[str, str],
        configuration: Configuration,
        expected_result: Mapping[str, str],
    ) -> None:
        with patch.object(ConfigurationParser, "parse", return_value=configuration):
            assert expected_result == CommandPreparer.prepare_multiple(
                commands=commands
            )
