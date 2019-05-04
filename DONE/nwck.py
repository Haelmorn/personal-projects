from Bio import Phylo
from io import StringIO
import re
import networkx


with open('rosalind_nwck.txt') as myFile:
    result = myFile.readlines()
    result = [i.replace("\n", "").split(" ") for i in result]
    result = sum(result, [])

for i in range(0, len(result), 4):
    handle = StringIO(result[i])
    tree = Phylo.read(handle, "newick")
    t =  Phylo.to_networkx(tree)
    A = [node for node in t.nodes() if node.name == result[i+1]][0]
    B = [node for node in t.nodes() if node.name == result[i+2]][0]
   
    print(len(networkx.shortest_path(t, A, B))-1, end=" ")
