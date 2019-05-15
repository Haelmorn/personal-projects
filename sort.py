from itertools import combinations

def read_and_pair(textfile):
    '''Reads input text file and returns a touple of 2 element touples'''
    with open(textfile, 'r') as file:
        TEMP = file.read().splitlines()
        TEMP = [line.split() for line in TEMP if line != ""]
    sets = (TEMP[0], TEMP[1])
    return sets

def rev(li, i_1, i_2):
    '''Takes a list, 'li', and reverses an interval between i1 and i2'''
    li[i_1:i_2+1] = li[i_1:i_2+1][::-1]
    return li


def how_similar(li, goal_comb):
    '''Takes a list, 'li', and checks how simillar it is to target list "goal_comb"'''
    similarity = 0
    for i in range(len(li[0])):
        if li[0][i] == goal_comb[i]:
            similarity += 1
    return similarity

def perms(list2, goal_comb):
    '''Generates a list of all possible lists created by reversing a subset of list "list2"
        then returns top 25% of all the reversals sorted by how simillar they are to
        "goal_comb"'''
    dict_of_reversals_similarity = {}
    for i, j in combinations(range(0, 11), 2):
        target = list2[:]
        current_perm = rev(target, i, j)
        current_similarity = how_similar(current_perm, goal_comb)
        dict_of_reversals_similarity[tuple(current_perm)] = current_similarity
    max_value = max(dict_of_reversals_similarity.values())
    maxes = [k for k, v in dict_of_reversals_similarity.items() if v >= max_value*0.5]

    return [list(i) for i in maxes]


def run():
    pair = read_and_pair("rosalind_sort.txt")
    if pair[0] == pair[1]:
        print(0)
    else:
        pair[0].append([])
        reversals = 1
        goal = pair[1]
        target = [[] for x in range(2)]
        target[0] = pair[0]
        permuts = perms(target[0], goal)
        while goal not in permuts:
            permuts = [perms(i, goal) for i in permuts]
            permuts = sum(permuts, [])
            permuts = [item for item in permuts if item[0:reversals] == goal[0:reversals] or item[-reversals:] == goal[-reversals:]]
            reversals += 1
        print(reversals)

run()
