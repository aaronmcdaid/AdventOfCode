"""
Day2b:

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""

import numpy as np

from advent_of_code.utils import load_input_lines

def parse(command: str): # a command is something like 'forward 5'
    direction, magnitude = command.split()
    magnitude = int(magnitude)
    return dict(
            down = lambda h, d, a: (h, d, a+magnitude), # "down X increases your aim by X units."
            up = lambda h, d, a: (h, d, a-magnitude), # "up X decreases your aim by X units."
            forward = lambda h, d, a: #"forward X does two things:"
                # It increases your horizontal position by X units.
                # It increases your depth by your aim multiplied by X
                (h + magnitude, d + a*magnitude, a),
            )[direction]

def run():
    i = load_input_lines('day2')
    
    h, d, a = 0, 0, 0 # the initial position, and aim
    for command in i:
        parsed_command = parse(command)

        # Apply the command to move our submarine
        h, d, a = parsed_command(h, d, a)

    # "What do you get if you multiply your final horizontal position by your final depth?"
    return h * d
