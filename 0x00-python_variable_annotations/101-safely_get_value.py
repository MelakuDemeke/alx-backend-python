#!/usr/bin/env python3
"""get value from dictionary"""
from typing import TypeVar, Mapping, Any, Optional, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Return value linked to key in dictionary or default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
