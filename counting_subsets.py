from math import factorial


def allsets(n):
    suma = 0
    for i in range(1, n + 1):
        suma += factorial(n) // (factorial(i) * factorial(n - i))
    return suma


print(allsets(831) % 1000000)
