from Bio.Seq import Seq
from Bio.Alphabet import generic_dna
from readros import read_rosalind as rr 

sequence = rr("test.txt")
sequence = list(sequence.values())
sequence = str(sequence[0])
print(sequence)
sequence = Seq(sequence, alphabet=generic_dna)
rev = sequence.reverse_complement()
print(rev)
c = []
for i in range(2, len(rev)):
    for j in range(0, len(rev)):
        if i + j <= len(rev):
            if sub[j:j+i] == rev[j:j+i]
                    c.append(len(sub))