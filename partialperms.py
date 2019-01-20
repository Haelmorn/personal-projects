from math import factorial

n = 100
k = 8
b = factorial(n)//factorial(n-k)
print(b % 1000000)