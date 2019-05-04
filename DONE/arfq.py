from math import sqrt

def carriers(n):
    """Calculates and returns how often non-dominant homozygote occurs in the population"""
    return n + 2 * sqrt(n) * (1-sqrt(n))

with open("rosalind_afrq.txt", "r") as file:
    IMPORTED_NUMS = file.readline().strip().split()

for i in IMPORTED_NUMS:
    curr = carriers(float(i))
    print('%.3f' % curr, end=' ')
