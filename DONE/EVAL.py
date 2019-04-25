n = 10
rest = 'AG'
gcs = [0.25, 0.5, 0.75]


for gc in gcs:
    prob = 1
    for char in rest:
        if char == "G" or char == "C":
            prob = prob * gc/2
        else:
            prob = prob * (0.5 - (gc/2))

    print('%0.3f' %  (n*prob), end=" ")