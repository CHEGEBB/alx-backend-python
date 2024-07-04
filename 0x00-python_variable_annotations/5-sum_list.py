#!/usr/bin/env python3
'''Module for sum_list function.
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Function that takes a list of floats as argument and
         returns their sum as a float.
    '''
    return float(sum(input_list))
