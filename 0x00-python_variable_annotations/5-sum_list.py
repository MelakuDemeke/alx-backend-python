#!/usr/bin/env python3
"""
Type-annotated function sum_list which takes a list input_list of floats
as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return sum of list of floats """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
