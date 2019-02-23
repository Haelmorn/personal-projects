from readros import read_rosalind as rr

seq = list(rr("test.txt").values())
print(seq)
seq = [x for x in seq if seq.count(x) == 1]
print(seq)

