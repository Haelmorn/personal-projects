import math
from scipy.stats.distributions import binom
n = 88
A = []
p = 0.5


def INDC(n,k,p):
    bc = binom.cdf(k,n,p)
    return math.log(bc,10)

def result(n):
    result = []
    for k in range(2*n):        
        result.append(INDC(2*n,k,0.5))
    return sorted(result,reverse=True)

for i in result(n):
    if '%.3f' % i == "-0.000":
        print("0.000", end = " ")
    else:
        print('%.3f' % i, end = " ")