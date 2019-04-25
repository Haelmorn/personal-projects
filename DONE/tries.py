sequences = ["ATAGA", "ATC", "GAT"]

trie = []
for element in sequences:
    for i in range(len(element)):
        if element[i] not in trie:
            trie.append(element[i])