#import a table with codon-aa pairs
from RNAtab import RNAtab as rna
#open file and join any split lines
with open("rosalind_prot.txt", "r") as f:
    text=''.join(line.rstrip() for line in f)
#split RNA string into codons
n = 3
codons = [text[i:i+n] for i in range(0, len(text), n)]
#create a list called protein
protein = []
#loop through the list, checking if current element is in dict rna
for i in range(0, len(codons)):
    if codons[i] in rna:
        #append a space on a STOP codon encounter
        if rna[codons[i]] == "STOP":
            protein.append(" ")
        #append the corresponding letter to protein if codon != STOP
        elif rna[codons[i]] != "STOP":
            protein.append(rna[codons[i]])

#print the output
print("".join(protein))
