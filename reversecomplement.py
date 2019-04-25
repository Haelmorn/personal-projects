def reverse_complement(sequence):
    rsequence = []
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            rsequence.append("T")
        elif sequence[i] == "T":
            rsequence.append("A")
        elif sequence[i] == "C":
            rsequence.append("G")
        elif sequence[i] == "G":
            rsequence.append("C")
    return "".join(rsequence[::-1])