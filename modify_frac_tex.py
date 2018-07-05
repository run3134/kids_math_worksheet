# __author__ = 'bren'

import re
import random
import itertools
import subprocess
splitter = re.compile(r'[{}]')
def gen_a_pair(lower_bd = 1, upper_bd=20):
    n1 = random.randint(lower_bd, upper_bd)
    n2 = random.randint(lower_bd+1, upper_bd)
    return (n1, n2)

def is_valid(a_pair):
    n1, n2 = a_pair
    if n1/n2>=1.5 or n1==n2:
        return False
    return True


def gen_a_valid_pair():
    while True:
        a_pair = gen_a_pair()
        if is_valid(a_pair):
            return a_pair


def gen_valid_pairs(n):
    return [gen_a_valid_pair() for i in range(n)]


def parse_a_line(a_line):
    return [pt for pt in splitter.split(line) if len(pt) > 0]



if __name__ == '__main__':
    output_lines = []
    with open("maggie.tex", 'r') as fh:
        for line in fh:
            if 'frac' not in line or '$' not in line:
                output_lines.append(line)
                continue

            res = [pt for pt in splitter.split(line) if len(pt) > 0 and not pt.isdigit()]
            digit_pairs = gen_valid_pairs(10)
            dig_pairs = ['{' + str(num) + '}' + '{' + str(den) + '}' for num, den in digit_pairs]
            combined = zip(res[:-1], dig_pairs)
            output_lines.append(''.join(list(itertools.chain(*combined))) + res[-1])

    with open("maggie_new.tex", 'w') as fh:
        for line in output_lines:
            fh.write(line)
    import os

    subprocess.check_call(['latex', 'maggie_new.tex'])
    subprocess.check_call(['dvipdfm', 'maggie_new.dvi'])
    files2rm = ['maggie.log', 'maggie.aux', 'maggie.out', 'maggie.synctex.gz',
                'maggie_new.aux', 'maggie_new.log', 'maggie_new.dvi', 'maggie_new.tex']
    for file in files2rm:
        if os.path.isfile(file):
            os.remove(file)
