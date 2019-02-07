import math


def allsets(n):
    suma = 0
    for i in range(1, n + 1):
        suma += math.factorial(n) // (math.factorial(i) * math.factorial(n - i))
    return suma


print(allsets(831) % 1000000)
