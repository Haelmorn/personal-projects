from math import factorial


sequence = "GGGGUAAAACGUCUGUGCGCAUAUACGGCAGCCGACAUGUAUUCCGUAAGCAUCUUCGGCGUUGGCUGCUGCUUGUUAUCCUCGGGCGCAGGAG"

A = sequence.count("A")
C = sequence.count("C")
U = sequence.count("U")
G = sequence.count("G")

minAU = min(A, U)
maxAU = max(A, U)
minCG = min(C, G)
maxCG = max(C, G)

score = (factorial(maxAU) // factorial(maxAU - minAU)) * (
    factorial(maxCG) // factorial(maxCG - minCG)
)
print(score)
