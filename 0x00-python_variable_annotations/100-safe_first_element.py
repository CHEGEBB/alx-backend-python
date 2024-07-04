#!/usr/bin/env python3
'''Module for safe_first_element function.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Function that takes a sequence lst of any type as argument and
        returns its first element if it exists, otherwise None.
    '''
    if lst:
        return lst[0]
    else:
        return None
