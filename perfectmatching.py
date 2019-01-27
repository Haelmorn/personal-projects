from readros import read_rosalind as rr

sequence = rr("test.txt")
sequence = list(sequence.values())
sequence = str(sequence[0])
a = len(sequence)/2
def perf(n):
    if n==1:
        return 1
    else:
        return (n-1) * perf(n-1)
g = perf(a)/2

print(f'{g:.50f}')