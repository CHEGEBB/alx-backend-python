#!/usr/bin/env python3
'''Module for zoom_array function.
'''
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Function that takes a tuple lst of integers and a factor as arguments
        and returns a list of integers that is the result of multiplying
        each integer by factor.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
