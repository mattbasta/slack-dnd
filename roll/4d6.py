for i1 in range(6):
    for j1 in range(6):
        for i2 in range(6):
            for j2 in range(6):
                a, b, x, y = i1 + 1, j1 + 1, i2 + 1, j2 + 1
                print "Rolled %d, %d, %d, and %d for %d and %d, totaling %d" % (
                    a, b, x, y,
                    a + b, x + y,
                    a + y + x + y)
