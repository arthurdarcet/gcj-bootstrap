import os
import sys

from . import config


def read(f=None):
    return f(config.in_stream.readline()) if f is not None else in_stream().readline()

def read_array(f=str, split=None):
    return map(f, read(f).split(split))

def write(s):
    config.out_stream.write(s)

def init(problem, input_size, input_id, in_file, out_file):
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
        down_path = os.path.join(config.download_dir, in_file)
        if not os.path.exists(in_file) and os.path.exists(down_path):
            os.system('mv "{}" "{}"'.format(down_path, in_file))
        config.in_stream = open(in_file, 'r')
    if out_file is not None:
        out_file = out_file.format(problem=problem, input_size=input_size, input_id=input_id)
        config.out_stream = open(out_file, 'w')
