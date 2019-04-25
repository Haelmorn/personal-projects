def read_rosalind(file):
    templist1 = []
    templist2 = []
    with open(file, "r") as f:
        current_line = ""
        for line in f:
            line = line.rstrip() # remover trailing '\n' character
            if line.startswith('>'):
                templist1.append(current_line)
                templist2.append(line[1:]) # drop the initial '>' character
                current_line = ""
            else:
                current_line = current_line + line
    templist2.append(current_line)
    del templist1[0]
    return [templist1, templist2]
