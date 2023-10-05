#!/usr/bin/env python3
'''accept string and int or float returns tuple'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''return tuple of string and square of int or float'''
    return (k, v**2)
