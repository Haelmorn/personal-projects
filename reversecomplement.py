def reverse_complement(sequence):
    sequence = sequence[::-1]
    rsequence = []
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            rsequence.append("U")
        elif sequence[i] == "U":
            rsequence.append("A")
        elif sequence[i] == "C":
            rsequence.append("G")
        elif sequence[i] == "G":
            rsequence.append("C")
    return "".join(rsequence)
    