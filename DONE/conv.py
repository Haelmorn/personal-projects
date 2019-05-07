with open('conv.txt', 'r') as file:
    elements = file.readlines()

A = elements[0].replace("\n","").split(" ")
B = elements[1].replace("\n","").split(' ')

minkowski_diff = []
for upper in A:
    for lower in B:
        curent_difference = abs(float(upper)-float(lower))
        minkowski_diff.append(round(curent_difference, 5))

diki ={}
for each in minkowski_diff:
    if each in diki.keys():
        diki[each] += 1
    else:
        diki[each] = 1

biggest_key = max(diki, key=diki.get)
print(diki[biggest_key])
print(biggest_key)