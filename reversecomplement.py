from sys import argv

sequence = argv[2]
typ = argv[1]

def reverse_complement(sequence):
    rsequence = []
    if typ == "DNA":
        for i in range(0, len(sequence)):
            if sequence[i] == "A":
                rsequence.append("T")
            elif sequence[i] == "T":
                rsequence.append("A")
            elif sequence[i] == "C":
                rsequence.append("G")
            elif sequence[i] == "G":
                rsequence.append("C")
    elif typ == "RNA":
        for i in range(0, len(sequence)):
            if sequence[i] == "A":
                rsequence.append("U")
            elif sequence[i] == "T":
                rsequence.append("A")
            elif sequence[i] == "C":
                rsequence.append("G")
            elif sequence[i] == "G":
                rsequence.append("C")
    return "".join(rsequence[::-1])

print(reverse_complement(sequence))