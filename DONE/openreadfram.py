from readros import read_rosalind as rr
from RNA_to_protein import translate
from RNAtab import RNAtab
from reversecomplement import reverse_complement

def findstartstop(DNA):
    #a - list of all sequences that begin with start codon
    #b - sequences from list cut before STOP codons
    #NOTE this function only returns a string if it has BOTH start and stop codons
    a = []
    b = []
    #Find all start codons and cut all previous bases
    for i in range(0, len(DNA)):
        if DNA[i:i+3] == "AUG":
            a.append(DNA[i:])
    #Find all stop codons and cut the string before them, resulting in a string in "AUG....." format
    for i in a:
        for j in range(0, len(i), 3):
            if i[j:j+3] == "UAA" or i[j:j+3] == "UGA" or i[j:j+3] == "UAG" and i[:j] not in b:
                b.append(i[:j])
                break
    return b


dna = list(rr("rosalind_splc.txt").values())
dna = dna[0]
dna = dna.replace("T", "U")
#Find all proteins in sequence (without reverse-complementing it)
prereverse = findstartstop(dna)
for i in range(0, len(prereverse)):
    prereverse[i] = translate(prereverse[i],3)
    prereverse[i] = "".join(prereverse[i])
rdna = reverse_complement(dna)
postreverse = findstartstop(rdna)
for i in range(0, len(postreverse)):
    postreverse[i] = translate(postreverse[i],3)
    postreverse[i] = "".join(postreverse[i])

whole = prereverse
for i in postreverse:
    if i not in whole:
        whole.append(i)
print(*whole, sep='\n')