#!/usr/bin/env python3
'''Module for to_kv function.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Function that takes a string k and an int OR float v as arguments
            and returns a tuple.
    '''
    return (k, float(v**2))
