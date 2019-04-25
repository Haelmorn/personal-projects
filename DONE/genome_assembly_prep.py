from readros import read_rosalind as rr

sequence = rr("test.txt")
SEQUENCES = list(sequence.values())

print(SEQUENCES)