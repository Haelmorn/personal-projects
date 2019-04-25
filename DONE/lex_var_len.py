import itertools

alphabet = "UTZDHAFWYV"
max_len = 3

words = []
for i in range(1, max_len+1):
    for cand in itertools.product(alphabet, repeat=i):
        words.append("".join(cand))

for occurence in sorted(words, key=lambda word: [alphabet.index(c) for c in word]):
    with open('test.txt', 'a') as the_file:
        the_file.write(f'{occurence}\n')