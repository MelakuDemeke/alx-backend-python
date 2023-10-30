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


def access_nested_map(nested_map, path):
    """
    Accesses a nested value in a dictionary using a sequence of keys.

    Args:
        nested_map (dict): A dictionary with nested values.
        path (tuple): A sequence of keys to access the nested value.

    Returns:
        The value at the end of the path.

    Raises:
        KeyError: If any key in the path is not found in the dictionary.
        TypeError: If the argument is not a dictionary or the path is not a tuple.
    """

    pass

