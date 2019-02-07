gc = 0.6
seq = "ATAGCCGA"
prob = 1


def probfun(n, gcontent, sequence, prob):
    for i in sequence:
        if i == 'A' or i == 'T':
            prob = prob * gcontent
        elif i == 'G' or i == 'C':
            prob = prob * (1 - gcontent)
    return 1 - prob


print(probfun(9000, gc, seq, 1))
