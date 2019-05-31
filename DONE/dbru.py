def reverse_complement(sequence):
    rsequence = []
    for i in range(0, len(sequence)):
        if sequence[i] == "A":
            rsequence.append("T")
        elif sequence[i] == "T":
            rsequence.append("A")
        elif sequence[i] == "C":
            rsequence.append("G")
        elif sequence[i] == "G":
            rsequence.append("C")
    return "".join(rsequence[::-1])


def read_and_parse(file):
    with open(file, 'r') as source:
        kmers = source.read().splitlines()
    kmers = list(set(kmers))
    for i in range(len(kmers)):
        kmers.append(reverse_complement(kmers[i]))
    
    return kmers

def get_adjacency(kmers):
    k1mers = [[mer[:-1], mer[1:]] for mer in kmers]
    to_set = [(mer1, mer2) for mer1, mer2 in k1mers]
    for pair1 in k1mers:
        for pair2 in k1mers:
            if pair1 != pair2 and pair1[1] == pair2[0]:
                to_set.append((pair1[0], pair2[0]))
    
    return set(to_set)

def main():
    kmer_list = read_and_parse("/home/haelmorn/Downloads/rosalind_pcov.txt")
    adjs = get_adjacency(kmer_list)
    with open("rosalind_dbru_out.txt", 'w+') as output:
        for pair in adjs:
            output.write(f"({pair[0]}, {pair[1]})\n")

if __name__ == "__main__":
    main()