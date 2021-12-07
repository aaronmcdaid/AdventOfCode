"""
Day1a:

How many measurements are larger than the previous measurement?
"""

import numpy as np

from advent_of_code.utils import load_input_lines

def run():
    i = load_input_lines('day1')
    measurements = [int(l) for l in i]
    diffs = np.ediff1d(measurements)
    number_of_positive_diffs = (diffs > 0).sum()
    return number_of_positive_diffs
