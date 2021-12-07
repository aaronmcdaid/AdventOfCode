"""
Day1b:

How many measurements are larger than the previous measurement, using the three-measurement window?
"""

import numpy as np

from advent_of_code.utils import load_input_lines

def run():
    i = load_input_lines('day1')
    measurements = [int(l) for l in i]
    sums_of_three = list(map(lambda x, y, z: x+y+z, measurements, measurements[1:], measurements[2:]))
    diffs = np.ediff1d(sums_of_three)
    return (diffs>0).sum()
