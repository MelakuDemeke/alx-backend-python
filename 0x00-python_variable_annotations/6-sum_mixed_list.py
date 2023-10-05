#!/usr/bin/env python3
'''return sum of mixed list of floats and ints'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    """ Return sum of list of floats """
    if mxd_lst is None:
        return 0
    else:
        return sum(mxd_lst)
