#get compared sequences as user input
s1 = input("Enter the first sequence: ")
s2 = input("Enter the second sequence: ")
#list all chars in seqences
s1l = list(s1)
s2l = list(s2)
#set counter to 0
hamming = 0
#iterate through both list checking for equality, increasing counter when chars are not equal
for i in range(0, len(s1)):
    if s1l[i] != s2l[i]:
        hamming += 1
    elif s1l[i] == s2l[i]:
        pass
print(f"{hamming}")
