from math import factorial

matchings = [("A", "U"), ("U", "A"), ("C", "G"), ("G", "C")]

def catalan(n):
    if n == 0:
        return 1
    else:
        return ((2*(2*n + 1))/(n+2)) * catalan(n-1)

seq = "AUAUAUAUAUAUAUAUAU"
suma = 0
n = len(seq)
m = []
for i in range (1, n+1):
    if (seq[0], seq[i]) in matchings:
        m.append(i)


for k in range(1, (n//2)+1):
    suma = suma + (catalan(k-1) * catalan(n - k))


#TODO: 1. Sprawdzić, gdzie można podzielić RNA na 2
#TOOD: 2. Policzyć matchingi po podzieleniu