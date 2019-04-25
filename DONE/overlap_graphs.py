from readros import read_rosalind as rr

textd = rr("rosalind_grph.txt")

listbeg = []
listend = []

for k, v in textd.items():
    listbeg.append(k)
    listend.append(k)
    listbeg.append(v[:3])
    listend.append(v[-3:])


dictpref = dict(zip(listbeg[::2], listbeg[1::2]))
dictsuf = dict(zip(listend[::2], listend[1::2]))

text_file = open("Output.txt", "w")

for k,v in dictsuf.items():
    for a,b in dictpref.items():
        if b == v and k != a:
            stri = k + " " + a
            text_file.write(stri)
            text_file.write("\n")

text_file.close()
