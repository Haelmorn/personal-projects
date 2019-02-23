from sys import argv

name, a, b, c, d, e, f = argv

off = [a, b, c, d, e, f]

for i in range(0, len(off)):
    off[i] = int(off[i])

offno = [2, 2, 2, 1.5, 1, 0]
suma = []

for i in range(0, len(off)):
    suma.append(off[i] * offno[i])

print(sum(suma))
