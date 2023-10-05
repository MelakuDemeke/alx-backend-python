#!/usr/bin/env python3
'''
type annotated function safe_first_element that takes a list
input_list ofany type elements and returns the first element
'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''returns first element of list'''
    if lst:
        return lst[0]
    else:
        return None
