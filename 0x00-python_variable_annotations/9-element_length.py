#!/usr/bin/env python3
'''accepts an iterable sequence and returns a list'''
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''returns a list of tuples containing elements and their length'''
    return [(i, len(i)) for i in lst]
