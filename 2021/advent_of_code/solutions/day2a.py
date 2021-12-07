"""
Day2a:

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

import numpy as np

from advent_of_code.utils import load_input_lines

def parse(command: str): # a command is something like 'forward 5'
    direction, magnitude = command.split()
    magnitude = int(magnitude)
    return dict(
            forward = lambda h, d: (h+magnitude, d),
            down = lambda h, d: (h, d+magnitude),
            up = lambda h, d: (h, d-magnitude),
            )[direction]

def run():
    i = load_input_lines('day2')
    
    h, d = 0, 0 # the initial position
    for command in i:
        parsed_command = parse(command)

        # Apply the command to move our submarine
        h, d = parsed_command(h, d)

    # "What do you get if you multiply your final horizontal position by your final depth?"
    return h * d
