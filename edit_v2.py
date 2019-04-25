
def newmethod852():
    """This module calculates the edit distance between two AA string"""
    import operator


    def how_simmilar(str1, str2):
        #"""This function compares two lists or string and returns how simmilar they are"""
        count = 0
        for i, item in enumerate(str2):
            if str1[i] == item or str1[i] == "0" or item == "0":
                count += 1
            else:
                pass
        return count

    def add_one(target, inp):
        #"""This function adds one char to the string and check if the simmilarity improves"""
        diki = {}
        for i in range(len(inp)+1):
            for j in range(1, len(target) - len(inp)+1):
                linp = list(inp)
                linp.insert(i, "0"*j)
                if how_simmilar(target, linp) >= PRE_SIMILARITY:
                    diki["".join(linp)] = how_simmilar(target, linp)
        return max(diki.items(), key=operator.itemgetter(1))[0]


    def calculate_edit_distance(proposed, actual):
        #"""Calculates actual edit distance"""
        edit_dictance = 0
        for i, item in enumerate(proposed):
            if actual[i] != item:
                edit_dictance += 1
        return edit_dictance


    LONGER_STR = "TGEIPSPAWHLCGLFKSGYMVSIKNAACTWPFHSEFAEFYHMCPHEWPVHLIHDE"
    SHORTER_STR = "WHLCGLFKSGYMVSIKNAACTWPHSEFAEF1PHE"
    PRE_SIMILARITY = how_simmilar(LONGER_STR, SHORTER_STR)

    while len(SHORTER_STR) < len(LONGER_STR):
        SHORTER_STR = add_one(LONGER_STR, SHORTER_STR)

    print(calculate_edit_distance(SHORTER_STR, LONGER_STR))

newmethod852()
