from readros import read_rosalind as rr
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = rr("test.txt")
dna = list(dna.values())[0]
