from readros import read_rosalind as rr
from itertools import product
import re
import sre_constants


seq = rr('test.txt').values()
seq = list(seq)
seq = str(seq[0])
bases = ['A', 'T', 'C', 'G']
new_data = []
for kmers in product(bases, repeat=4):
    new_data.append(''.join(kmers))


kmer_list = []
seq_divided = []
new_data.sort()
for i in range(len(seq)):
    seq_divided.append(seq[i:i+4])

for kmer in new_data:
    kmer_list.append(seq_divided.count(kmer))

print(*kmer_list)