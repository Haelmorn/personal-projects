from masstable import masstable as mass

protein = input("Enter protein string: ")
masses = []
for i in range(0, len(protein)):
    if protein[i] in mass:
        masses.append(mass[protein[i]])

print(round(sum(masses), 3))
