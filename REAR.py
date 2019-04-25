import random

with open('test.txt', 'r') as file:
        temp = file.read().splitlines()
        temp = [line.split() for line in temp if line != ""]

def swapperooo(str_A, str_B):
    c = 0
    for i in range(0, len(str_A)-1):
        if str_A[i] != str_B[i]:
            post = str_B.index(str_A[i])
            str_B[i], str_B[post] = str_B[post], str_B[i]
            c += 1
    return c

for i in range(0, len(temp), 2):
        print(swapperooo(temp[i], temp[i+1]), end = ' ')

print()
