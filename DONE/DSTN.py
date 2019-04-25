from readros import read_rosalind as rr
import numpy as np

seq = list(rr("test.txt").values())

dst = np.zeros((len(seq), len(seq)))

def difference(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c/len(a)

for i in range(len(seq)):
    for j in range(len(seq)):
        dst[i][j] = difference(seq[i], seq[j])

for row in dst:
    for a in row:
        print('{0:.5f}'.format(a), end = " ")
    print()