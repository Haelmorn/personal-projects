gc = 0.558360
seq = "AGCGTAAA"
prob = 1


def probfun(gcontent, sequence, prob):
    for i in sequence:
        if i == 'A' or i == 'T':
            prob = (prob * (1 - gcontent))/2
        elif i == 'G' or i == 'C':
            prob = (prob * gcontent)/2
            
    return prob


ans = 1 - (1- probfun(gc, seq, 1))** 83684
print('%0.3f' %  ans)
