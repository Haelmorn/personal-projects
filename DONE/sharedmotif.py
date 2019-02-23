from readros import read_rosalind as rr 

b = list(rr("test.txt").values())

a = b[0]
b.pop(0)
c = []
for i in range(2, len(a)):
    for j in range(0, len(a)):
        if i + j <= len(a):
            sub = a[j:j+i]
            if all(sub in text for text in b):
                if sub not in c:
                    c.append(sub)

print(max(c, key=len))