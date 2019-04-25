#import a table with codon-aa pairs
from RNAtab import RNAtab
#open file and join any split lines
def prep(file):
    with open("file", "r") as f:
        text=''.join(line.rstrip() for line in f)
#split RNA string into codons
def translate(rna, n):
    codons = [rna[i:i+n] for i in range(0, len(rna), n)]
    #create a list called protein
    protein = []
    #loop through the list, checking if current element is in dict RNAtab
    for i in range(0, len(codons)):
        if codons[i] in RNAtab:
            #append a space on a STOP codon encounter
            if RNAtab[codons[i]] == "STOP":
                protein.append(" ")
            #append the corresponding letter to protein if codon != STOP
            elif RNAtab[codons[i]] != "STOP":
                protein.append(RNAtab[codons[i]])
    return protein
    
if __name__ == "__main__":
    prep(rosalind_splc.txt)
