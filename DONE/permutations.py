import itertools

num = int(input("enter no.: "))
num = range(1, num+1)
perms = list(itertools.permutations(num))
print(len(perms))
for i in range(0, len(perms)):
    print(*perms[i], sep = " ")