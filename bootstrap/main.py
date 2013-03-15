#!/usr/bin/env python
# Bootstrap from https://github.com/arthurdarcet/gcj-bootstrap
# Usage: main.py [[input_size]] input_id]

from lib import read, read_array, write


def main():
    return 42


# Parameters:
PROBLEM = None
INPUT_SIZE = 'small' # None to read from command line
INPUT_ID = 'practice' # None to read from command line
INPUT_FILE = '{problem}-{input_size}-{input_id}.in' # None for stdin
OUTPUT_FILE = '{problem}-{input_size}-{input_id}.out' # None for stdout

# Bootstrap:
import lib
if __name__ == '__main__':
    lib.init(PROBLEM, INPUT_SIZE, INPUT_ID, INPUT_FILE, OUTPUT_FILE)
    T = read(int)
    for t in range(1,T+1):
        write('Case #{0}: {1}\n'.format(t, main()))

