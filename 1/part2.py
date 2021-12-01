# Read input file and convert into list of integers
i = [int(l.strip()) for l in open('input.txt', 'r').readlines()]
# Create a list of 3-element sliding window sums
s = [sum(w) for w in zip(i[:-2], i[1:-1], i[2:])]
# Pairwise compare successive elements and print total number of increases
print(sum(1 if a < b else 0 for a, b in zip(s[:-1], s[1:])))
