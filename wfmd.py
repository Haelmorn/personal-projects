from math import factorial
from scipy.special import binom 

N = 4
m = 6
g = 2
k = 1


p = m/(2*N)
q = 1 - p
prob = 0
for i in range(0,k+1):
    prob += binom(2*N, i) * (p**i) * q**((2*N) - i)
    print(prob)