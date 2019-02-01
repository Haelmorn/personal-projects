from itertools import product

seq = ("A","B","C","D","E","F", "G", "H", "I")
n = 3

for perms in product(seq, repeat = n):
    print(''.join(perms))
print("\n")