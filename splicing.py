from readros import read_rosalind as rr
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna


codons = list(rr("rosalind_splc.txt").values())
DNAstring = codons[0]
codons.pop(0)
for i in range(0, len(codons)):
    if codons[i] in DNAstring:
        DNAstring = DNAstring.replace(codons[i], '')

myprot = Seq(DNAstring, generic_dna)
prot = myprot.translate()
print(prot)