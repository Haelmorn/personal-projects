#DNA string to look for the motif
input = """ """

#sequence to be found
seq = "AAGCATGAA"
#loop through subsets of chars and print the iterator (+1, since arrays start at 0)
for i in range(0, len(input)):
    if input[i:i+len(seq)] == seq:
        print(f"{i+1}", end=" ")
