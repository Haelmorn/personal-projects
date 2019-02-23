import math

k = 6
n = 15


def Ber(gen, num_offspring):
    return (math.factorial(2 ** gen) / (math.factorial(num_offspring) * math.factorial((2 ** gen) - num_offspring))) * (
                0.25 ** num_offspring) * (1 - 0.25) ** ((2 ** gen) - num_offspring)


prob = 0.0
while n <= (2 ** k):
    prob += Ber(k, n)
    n += 1

print(round(prob, 3))
