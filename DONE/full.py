with open("/home/haelmorn/Downloads/rosalind_full.txt",'r') as data:
    numbers = data.read().splitlines()

numbers = [float(number.replace("\n", "")) for number in numbers]
total_mass = numbers[0]
temp = []
for i in range(1, len(numbers)):
    for j in range(1, len(numbers)):
        temp.append((numbers[i], numbers[j]))

numbers = [pair[0] for pair in temp if round(pair[0] + pair[1],5) == round(numbers[0],5)]
numbers = [round(number, 6) for number in numbers]
numbers.insert(0, total_mass)
masstable = {
"A": 71.03711,
"C": 103.00919,
"D": 115.02694,
"E": 129.04259,
"F": 147.06841,
"G": 57.02146,
"H": 137.05891,
"I": 113.08406,
"K": 128.09496,
"L": 113.08406,
"M": 131.04049,
"N": 114.04293,
"P": 97.05276,
"Q": 128.05858,
"R": 156.10111,
"S": 87.03203,
"T": 101.04768,
"V": 99.06841,
"W": 186.07931,
"Y": 163.06333
}

numbers = [number - numbers[1] for number in numbers[1:]]
masstable = {round(k,2):v for v,k in masstable.items()}

for i in range(len(numbers[1:])-1):
    c = round(numbers[i],2)
    if c in masstable.keys():
        print(masstable[c], end='')
        numbers = [mass - numbers[i] for mass in numbers]