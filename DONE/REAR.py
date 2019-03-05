import random

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
B = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]

C = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
D = [5, 2, 3, 1, 7, 4, 10, 8, 6, 9]


def swapperooo(str_A, str_B):
    c = 0
    for i in range(0, len(str_A)-1):
        if str_A[i] != str_B[i]:
            post = str_B.index(str_A[i])
            str_B[i], str_B[post] = str_B[post], str_B[i]
            c += 1
    return c

