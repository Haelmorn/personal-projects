from sys import argv

for each in argv[1:]:
    p = float(each)
    prob = 2 * p * (1-p)
    print('%.4f' % prob, end=" ")
