#!/usr/bin/env python
import os, sys

def main():
    return 42


# Parameters:
PROBLEM = None
INPUT_SIZE = 'small'
INPUT_ID = '-practice'
INPUT_FILE = '{problem}-{input_size}{input_id}.in' # None for stdin
OUTPUT_FILE = '{problem}-{input_size}{input_id}.out' # None for stdout
DOWNLOAD_DIR = os.path.expanduser('~/Downloads')

# Bootstrap:
in_stream, out_stream = sys.stdin, sys.stdout
out_stream = sys.stdout
def read(f=None):
    return f(in_stream.readline()) if f is not None else in_stream.readline()

def read_array(f=str, split=None):
    return [f(i) for i in read().split(split)]

def write(s):
    out_stream.write(s)

def init(problem, input_size, input_id, in_file, out_file):
    global in_stream, out_stream
    if in_file is not None or out_file is not None:
        if len(sys.argv) == 3:
            input_size = sys.argv[1]
            input_id = sys.argv[2]
        elif len(sys.argv) == 1 and (input_size is None or input_id is None):
            sys.stderr.write('Usage: main.py [[input_size] input_id]\n')
            sys.stderr.write('Error: input_size and input_id must be provided in main.py or on the command line\n')
            sys.exit(1)
        elif len(sys.argv) == 2:
            if input_size is None:
                input_size = sys.argv[1]
            else:
                input_id = sys.argv[1]
    if in_file is not None:
        in_file = in_file.format(problem=problem, input_size=input_size, input_id=input_id)
        down_path = os.path.join(DOWNLOAD_DIR, in_file)
        if not os.path.exists(in_file) and os.path.exists(down_path):
            os.system('mv "{}" "{}"'.format(down_path, in_file))
        in_stream = open(in_file, 'r')
    if out_file is not None:
        out_file = out_file.format(problem=problem, input_size=input_size, input_id=input_id)
        out_stream = open(out_file, 'w')

if __name__ == '__main__':
    init(PROBLEM, INPUT_SIZE, INPUT_ID, INPUT_FILE, OUTPUT_FILE)
    T = read(int)
    for t in range(1,T+1):
        write('Case #{0}: {1}\n'.format(t, main()))

