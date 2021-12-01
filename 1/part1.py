# Read input file and convert into list of integers
i = [int(l.strip()) for l in open('input.txt', 'r').readlines()]
# Pairwise compare successive elements and print total number of increases
print(sum(1 if a < b else 0 for a, b in zip(i[:-1], i[1:])))
