from readros import read_rosalind as rr 
from reversecomplement import reverse_complement

sequence = rr("test.txt")
sequence = list(sequence.values())
sequence = str(sequence[0])
diki = []
for i in range(12, 3, -2):
        for j in range(0, len(sequence)-i+1):
                seq = sequence[j:j+i]
                if seq == reverse_complement(seq):
                        diki.append([j+1, i])

for pair in diki:
        print(pair[0], "\t", pair[1])
