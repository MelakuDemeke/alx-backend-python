#!/usr/bin/env python3

def element_length(lst: List[Union[str,int,float ]]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
