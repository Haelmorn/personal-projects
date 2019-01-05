#protfreq contains RNAtab which is a dict containing aa names (A, B, T etc.) as keys and then a number of codons they are coded by as val
from protfreq import RNAtab as tab
from functools import reduce
import operator, math
#get the input and list all chars
listaa = []
prot = input("Enter aa sequence: ")

#iterate through all chars and append the responding val to a list
for i in range(0, len(prot)):
    if prot[i] in tab:
        listaa.append(tab[prot[i]])
    elif prot[i] not in tab:
        print("DUPA")

for i in range(0, len(listaa)):
    if i == 0:
        l = 1 * listaa[i]
    elif i != 0:
        l = l * listaa[i]

l = l*3 % 1000000

print(f"{l}")
