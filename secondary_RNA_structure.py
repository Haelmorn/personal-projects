from math import factorial


sequence = (
    "GAAGGCCCUAUUAUGGUAGCCGCACUACCCGUCUCGCAGGACUCGAGCAGAUGUAUAGUUGAGCCGCCGUAUGCGC"
)
A = sequence.count("A")
C = sequence.count("C")

fact = factorial(A) * factorial(C)
print(fact)
