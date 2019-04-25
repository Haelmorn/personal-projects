def read_rosalind(file):
    templist = []
    with open(file, "r") as f:
        current_line = ""
        for line in f:
            line = line.rstrip() # remover trailing '\n' character
            if line.startswith('>'):
                templist.append(current_line)
                templist.append(line[1:]) # drop the initial '>' character
                current_line = ""
            else:
                current_line = current_line + line
    templist.append(current_line)
    del templist[0]
    dictionary = dict(zip(templist[::2], templist[1::2]))
    return dictionary
