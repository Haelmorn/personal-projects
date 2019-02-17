# Calculate the percentage of G and C bases in the DNA string
def gcpercentage(string):
    G = int(string.count("G"))
    C = int(string.count("C"))
    percentage = (G + C) / float(len(string))
    return percentage

if __name__ == "__main__":
    # prep text for modification
    with open("test.txt", "r") as f:
        text = f.readlines()
    for i in range(0, len(text)):
        text[i] = text[i].replace("\n", "")
        text[i] = text[i].replace(">", "")

    # create a dict from the prepared text
    textd = dict(zip(text[::2], text[1::2]))

    # create another dict containing DNA string names as keys and calculated GC percentage values as values
    a = {}
    for k, v in textd.items():
        a[k] = gcpercentage(v)

    # find and print the highest GC percentage alongside with its key
    maximum = max(a, key=a.get)
    print(maximum, "\n", a[maximum] * 100)

