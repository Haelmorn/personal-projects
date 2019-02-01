from readros import read_rosalind as rr

sequences =  list(rr("test.txt").values())
frame = sequences[0]
val = sequences[1]

indices = []
def get_indices():
    last = 0
    for i in val:
        for a in range(len(frame)):
            if frame[a] == i and a > last:
                indices.append(a+1)
                last = a
                break
get_indices()
print(*indices)