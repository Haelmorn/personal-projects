import regex as re
from urllib.request import urlopen
from bs4 import BeautifulSoup


def solve(s):
    s = s.split('\n', 1)[-1]
    if s.find('\n') == -1:
        return ''
    return s.rsplit('\n', 1)[0]
listp = []
listc = []

templist = []
with open("rosalind_mprt.txt", "r") as f:
    for line in f:
        line = line.rstrip() # remover trailing '\n' character
        templist.append(line)


for i in range(0, len(templist)):
    proten = templist[i]
    url = f"https://www.uniprot.org/uniprot/{proten}.fasta"
    content = urlopen(url).read()
    soup = BeautifulSoup(content, features="html5lib")
    info = soup.get_text()
    protname = re.search(r'\|(.*)\|', info).group(1)
    protcode = solve(info).replace("\n", "")
    listp.append(protname)
    listc.append(protcode)
regex = re.compile("N[^P](S|T)[^P]")

for i in range(0, len(listc)):
    occlist = [m.start(0)+1 for m in re.finditer(regex, listc[i], overlapped=True)]
    if occlist:
        print(templist[i])
        print(*occlist)




