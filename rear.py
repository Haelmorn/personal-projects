import random
from itertools import combinations
from profilestats import profile

with open('rosalind_rear.txt', 'r') as file:
    temp = file.read().splitlines()
    temp = [line.split() for line in temp if line != ""]


def rev(li, i1, i2):
    li[i1:i2+1] = li[i1:i2+1][::-1]
    return li

@profile(print_stats=20)
def similarity(li, goal_comb):
    #similarity = 0
    #for i in range(len(li)):
        #if li[i] == goal_comb[i]:
            #similarity += 1
    #return similarity
    return len([i for i, j in zip(li, goal_comb) if i == j])

def perms(list2, goal_comb):
    diki = {}
    for i, j in combinations(range(0, 11), 2):
        target = list2[:]
        current_perm = rev(target, i, j)
        current_similarity = similarity(current_perm, goal_comb)
        diki[tuple(current_perm)] = current_similarity
    maxValue = max(diki.values())
    maxes = [k for k, v in diki.items() if v >= maxValue*0.5]

    return [list(i) for i in maxes]


def run():
    sets = ((temp[0], temp[1]), (temp[2], temp[3]), (temp[4], temp[5]), (temp[6], temp[7]), (temp[8], temp[9]))
    for pair in sets:
        if pair[0] == pair[1]:
            print(0)
        else:
            reversals = 1
            goal = pair[1]
            permuts = perms(pair[0], goal)
            while goal not in permuts:
                permuts = [perms(i, goal) for i in permuts]
                permuts = sum(permuts, [])
                permuts = [item for item in permuts if item[0:reversals] == goal[0:reversals] or item[-reversals:] == goal[-reversals:]]
                reversals += 1
            print(reversals)

run()