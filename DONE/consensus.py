from readros import read_rosalind as rr
import numpy as np

text = rr("test.txt")
subs = list(text.values())
subst = [list(i) for i in subs]
subst = np.array(subst)
subst = subst.transpose()

subst = subst.tolist()

cstr = []
alist = []
clist = []
glist = []
tlist = []
for i in range(0, len(subst)):
    ca = subst[i].count("A")
    alist.append(ca)
for i in range(0, len(subst)):
    ca = subst[i].count("C")
    clist.append(ca)
for i in range(0, len(subst)):
    ca = subst[i].count("T")
    tlist.append(ca)
for i in range(0, len(subst)):
    ca = subst[i].count("G")
    glist.append(ca)

for i in range(0, len(alist)):
    cslist = [alist[i], clist[i], tlist[i], glist[i]]
    if max(cslist) == alist[i]:
        print("A", end="")
    elif max(cslist) == clist[i]:
        print("C", end="")
    elif max(cslist) == tlist[i]:
        print("T", end="")
    elif max(cslist) == glist[i]:
        print("G", end="")
print("\n")

print(f"A: ", end="")
print(*alist)
print(f"C: ", end="")
print(*clist)
print(f"G: ", end="")
print(*glist)
print(f"T: ", end="")
print(*tlist)
