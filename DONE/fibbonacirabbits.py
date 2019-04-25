n = 88
m = 20
age = [1] + [0] * (m - 1)
for i in range(0, n - 1):
    age = [sum(age[1:])] + age[:-1]
print(sum(age))
