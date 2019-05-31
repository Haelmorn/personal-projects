kseq1 = "PLEASANTLY"
seq2 = "MEANLY"

def edit_distance(seq1, seq2): # Wagner-Fischer algorithm
    cur = list(range(len(seq1)+1))
    for j, s in enumerate(seq2):
        last, cur = cur, [j+1] 
        for i, t in enumerate(seq1):
            cur.append(last[i] if s==t else min([last[i+1], last[i], cur[-1]]) + 1)
    return cur[-1]

print(edit_distance(seq1,seq2))