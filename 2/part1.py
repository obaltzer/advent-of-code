# Using groupby from itertools
from itertools import groupby
# Read input file, group by command and aggregate units
d = { c: sum([int(v[1]) for v in vs]) for c, vs in groupby(sorted([l.strip().split() for l in open('input.txt', 'r').readlines()]), key=lambda x: x[0]) }
print(d['forward'] * (d['down'] - d['up']))
