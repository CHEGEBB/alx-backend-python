#!/usr/bin/env python3
'''Module for element_length function.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Function that takes an iterable of sequences as argument and
        returns a list of tuples where each tuple contains a sequence
        and its length.
    '''
    return [(i, len(i)) for i in lst]
