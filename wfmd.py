from math import factorial

N = 4
m = 6
g = 2


p = m/(2*N)
q = 1 - p
prob = 0
for k in range(1, 2*N + 1):
    prob = prob + (factorial(2*N)/(factorial(k)*factorial(2*N - k)))*(p**k)*q**(2*N - k)

print(prob)