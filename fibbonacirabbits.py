def fibbonaci(n):
    if n < 2:
        return n
    return fibbonaci(n-2) + fibbonaci(n-1)
n = 40
m = 16
all = 0
for i in range(0, n-m+1):
    all += fibbonaci(i)

sol = fibbonaci(n) - all
print(sol)
