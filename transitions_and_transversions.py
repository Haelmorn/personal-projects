from readros import read_rosalind as rr

sequences = list(rr("test.txt").values())

transitions = 0
transversions = 0
for i in range(0, len(sequences[0])):
    if sequences[0][i] == "A" and sequences[1][i] == "G" or sequences[0][i] == "G" and sequences[1][i] == "A":
        transitions += 1
    elif sequences[0][i] == "C" and sequences[1][i] == "T" or sequences[0][i] == "T" and sequences[1][i] == "C":
        transitions += 1
    elif sequences[0][i] != sequences[1][i]:
        transversions += 1

print('{0:.11f}'.format(transitions/transversions))