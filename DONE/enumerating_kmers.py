import itertools

seq = ("A", "B", "C", "D", "E", "F", "G", "H", "I")
n = 3

for perms in itertools.product(seq, repeat=n):
    print("".join(perms))
print("\n")
