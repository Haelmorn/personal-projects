def subsequence(seq):
    if not seq:
        return seq

    M = [None] * len(seq)  # offset by 1 (j -> j-1)
    P = [None] * len(seq)
    L = 1
    M[0] = 0

    # Looping over the sequence starting from the second element
    for i in range(1, len(seq)):
        lower = 0
        upper = L

        # Since the binary search will not look at the upper bound value,
        # we'll have to check that manually
        if seq[M[upper - 1]] < seq[i]:
            j = upper

        else:
            # actual binary search loop
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if seq[M[mid - 1]] < seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower  # this will also set the default value to 0

        P[i] = M[j - 1]

        if j == L or seq[i] < seq[M[j]]:
            M[j] = i
            L = max(L, j + 1)

    # Building the result: [seq[M[L-1]], seq[P[M[L-1]]], seq[P[P[M[L-1]]]], ...]
    result = []
    pos = M[L - 1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]  # reversing


if __name__ == "__main__":
    fid = open('test.txt', 'r')
    # fid = open('main.txt','r')
    fout = open('out.txt', 'w')
    n = int(fid.readline().strip())
    s = [int(x) for x in fid.readline().split()]

    # print s
    inc = subsequence(s)
    dec = subsequence(s[::-1])[::-1]

    fout.write('%s\n%s' % (str(inc).strip('[]').replace(',', ''), str(dec).strip('[]').replace(',', '')))
