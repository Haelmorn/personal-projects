from Bio import Phylo
from io import StringIO
import re
import networkx


with open('rosalind_nkew.txt') as myFile:
    result = myFile.readlines()
    result = [i.replace("\n", "").split(" ") for i in result]
    result = sum(result, [])

for i in range(0, len(result), 4):
    handle = StringIO(result[i])
    tree = Phylo.read(handle, "newick")
    print(int(tree.distance(result[i+1], result[i+2])), end=" ")