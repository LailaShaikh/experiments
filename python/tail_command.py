"""
Run this program:

python tail_command.py <abs_file_path>

Now if you append any line on this file, you would see the live beat in your shell instantly

"""

import time
import sys

def tail(fn):
    def check_new_line(fp):
        fp.seek(0, 2)
        while True:
            curr_line = fp.readline()
            if curr_line:
                yield curr_line
            else:
                time.sleep(0.2)

    for line in check_new_line(open(fn, 'rb')):
        print line

if __name__ == '__main__':
    file_name = sys.argv[1]
    tail(file_name)
