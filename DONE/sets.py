n = 1
A = {}
B = {}
U = set(range(1, n+1))

text_file = open("Output.txt", "w")

text_file.write(str(A | B))
text_file.write("\n")
text_file.write(str(A & B))
text_file.write("\n")
text_file.write(str(A - B))
text_file.write("\n")
text_file.write(str(B - A))
text_file.write("\n")
text_file.write(str(U - A))
text_file.write("\n")
text_file.write(str(U - B))
text_file.write("\n")
