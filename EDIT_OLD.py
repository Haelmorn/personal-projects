from readros import read_rosalind as rr
from itertools import permutations
import operator

def similarity(str1, str2):
    count = 0
    for i in range(len(str1)):
        if str1[i] == str2[i] or str1[i] == "0" or str2[i] == "0":
            count += 1
        else:
            pass
    return count

def gen_eq_lens(str1, str2):
    dif = len(str1) - len(str2)
    if dif != 0:
        gens = []
        for element in permutations(range(0, len(str1)), dif):
            if similarity(element, str1):
                str2l = list(str2)
                for el in element:
                    str2l.insert(el, "0")
                    gens.append(str2l)
        return iter(gens)
    else:
        return "0"*len(str1)

def check_for_similarity(li, st):
    sim_dict = {}
    for elem in li:
        sim_dict["".join(elem)] = similarity(elem, st)
    return max(sim_dict.items(), key=operator.itemgetter(1))[0]

def calculate_edit_distance(proposed, actual):
    edit_dictance = 0
    for i, item in enumerate(proposed):
        if actual[i] != item:
            edit_dictance += 1
    return edit_dictance


longer_str = "Pleasantly"
shorter_str = "Meanly"
check_list = gen_eq_lens(longer_str, shorter_str)
result = check_for_similarity(check_list, longer_str)
print(calculate_edit_distance(result, longer_str), result)
