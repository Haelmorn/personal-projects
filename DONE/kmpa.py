from readros import read_rosalind as rr


word = list(rr('test.txt').values())[0]

table = [0] * (len(word)+1)


def kmp_table(W, T):
    pos = 1
    cnd = 0

    T[0] = -1

    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd] + 1
        else:
            T[pos] = cnd
            cnd = T[cnd]
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos = pos + 1
        cnd = cnd +1
    
    T[pos] = cnd
    return T

a = [abs(x) for x in kmp_table(word, table)]
del a[0]

for el in a:
    with open('output.txt', 'a') as the_file:
        the_file.write(f"{el} ")