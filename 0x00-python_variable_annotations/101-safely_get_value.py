#!/usr/bin/env python3
'''Module for safely_get_value function.
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''Function that takes a Mapping dct, a key and an optional default value
        and returns the value associated with key in dct if it exists,
        otherwise the default value.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
