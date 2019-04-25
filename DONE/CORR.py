from readros import read_rosalind as rr
from reversecomplement import reverse_complement

seq = list(rr("test.txt").values())


def prep(seq_list):
    occ = []
    err = []
    for el_a in seq_list:
        c = 0
        for el_b in seq_list:
            if el_a == el_b or el_a == reverse_complement(el_b):
                c += 1
        occ.append(c)

    for i in range(len(seq_list)):
        if occ[i] == 1:
            err.append(seq_list[i])

    return err


def hamming_distance(str_1, str_2):
    c = 0
    for i in range(len(str_1)):
        if str_1[i] != str_2[i]:
            c += 1
    return c


def find_matches(error, correct):
    matches = {}
    for er in error:
        for cor in correct:
            if hamming_distance(er, cor) == 1:
                matches[er] = cor
            elif hamming_distance(er, reverse_complement(cor)) == 1:
                matches[er] = reverse_complement(cor)
    return matches

def main(sequences):
    errors = prep(sequences)
    corrects = [x for x in sequences if x not in errors]
    matches = find_matches(errors, corrects)
    
    for k, v in matches.items():
        print(k, end='')
        print("->", end='')
        print(v)


if __name__ == "__main__":
    main(seq)
