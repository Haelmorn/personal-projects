from itertools import permutations

n = 4 #Number from 1 to 6

m = list(range(1, n+1)) #List of all numbers from 1 to n for reference
seq = list(range(-n, n+1)) #Proper sequence with both + and - signs
seq.remove(0) #Remove the unnecessary 0 from the list

perms = list(permutations(seq, n)) #Generate the list of all premuatations
perm = perms[:] #Create a copy of said list 

for sets in perms: #Loop over all sets of numbers
    for number in m:
        if number in sets and -number in sets: #Check if each number comes with both + and - sign in the list, if so: delete it from copy
            perm.remove(sets)
            break


print(len(perm)) #Print the number of permuatations and all permutations ('*' removes commas, parentheses etc.)
for i in perm:
    print(*i)