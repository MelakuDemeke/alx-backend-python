#!/usr/bin/env python3
"""
This module contains unit tests for the utils module.

The utils module provides various utility functions that are used throughout
the project.These tests ensure that the functions in the utils module behave
as expected and do not introduce any regressions.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Accesses a nested value in a dictionary using a sequence of keys.

    Args:
        nested_map (dict): A dictionary with nested values.
        path (tuple): A sequence of keys to access the nested value.

    Returns:
        The value at the end of the path.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test function to check if the access_nested_map function returns
        the expected value.

        Args:
        - nested_map: A dictionary representing a nested map.
        - path: A list of keys representing the path to a value
        - expected: The expected value at the end of the path.

        Returns:
        - None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
