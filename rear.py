import random
from itertools import combinations
import copy

#with open('test.txt', 'r') as file:
#        temp = file.read().splitlines()
#        temp = [line.split() for line in temp if line != ""]

A = [[1,2,3,4,5,6,7,8,9,10], [3,1,5,2,7,4,9,6,10,8]]

B = [[3,10,8,2,5,4,7,1,6,9], [5,2,3,1,7,4,10,8,6,9]]


def rev(li, i1, i2):
    li[i1:i2+1] = li[i1:i2+1][::-1]
    return li

def similarity(li, goal_comb):
    similarity = 0
    for i in range(len(li)):
        if li[i] == goal_comb[i]:
            similarity += 1
    return similarity/len(li)

def perms(list2, goal_comb):
    diki = {}
    for i, j in combinations(range(0, 11), 2):
        target = copy.deepcopy(list2)
        current_perm = rev(target, i, j)
        current_similarity = similarity(current_perm, goal_comb)
        diki[tuple(current_perm)] = current_similarity
    maxValue = max(diki.values())
    maxes = [k for k, v in diki.items() if v == maxValue]

    return [list(i) for i in maxes]


def run():
    reversals = 1
    goal = A[1]
    permuts = perms(A[0], goal)
    while goal not in permuts:
        permuts = [perms(i, goal) for i in permuts]
        reversals += 1
    print(reversals)
