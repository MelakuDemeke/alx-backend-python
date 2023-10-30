"""Module for testing the Client class."""

import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, resp: Dict, mocked_fxn: MagicMock) -> None:
        pass

