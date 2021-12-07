def load_input_lines(day): # e.g. day == "day1"
    with open(f'./advent_of_code/inputs/{day}', 'r') as h:
        return [l.strip() for l in h.readlines()]
