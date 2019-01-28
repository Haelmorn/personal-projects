import math


def product(list):
    p = 1
    for i in list:
        p *= i
    return p


seq = """GTCGACGGAAATGGAGCTCAATGACCCATTCAAAGG
CGGCGCTCCGTTTGAAACTAGTAAGATCTGCAAATTTTTAACAG"""
gctable = [0.066, 0.176, 0.199, 0.278, 0.314, 0.432, 0.457, 0.558, 0.599,
           0.647, 0.696, 0.806, 0.874, 0.893]
prelogtab = []
perc = {}
for element in gctable:
    perc.update({"G": element/2})
    perc.update({"C": element/2})
    perc.update({"A": (1 - element)/2})
    perc.update({"T": (1 - element)/2})
    prelog = []
    for i in seq:
        prelog.append(perc[i])
    prelogtab.append(prelog)

for el in range(len(prelogtab)):
    prelogtab[el] = round(math.log10(product(prelogtab[el])), 3)

print(*prelogtab)