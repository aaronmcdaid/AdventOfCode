from importlib import import_module
import sys
from timeit import default_timer

def main():
    _, script_name = sys.argv # e.g. day1a or day1b

    m = import_module(f'advent_of_code.solutions.{script_name}')
    before = default_timer()
    result = m.run()
    after = default_timer()
    runtime_in_seconds = (after - before)
    print(f'''Result for {script_name}: {result}
Runtime {runtime_in_seconds:.2g}s''')



if __name__ == '__main__':
    main()
