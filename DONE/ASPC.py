from math import factorial

n = 1903
m = 1398
most = 0
for k in range(m, n+1):
    most += factorial(n) // (factorial(k)*factorial(n-k))

print(most % 1000000)