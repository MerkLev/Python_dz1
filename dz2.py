X1 = [True, False]
Y1 = [True, False]
Z1 = [True, False]

for X in X1:
    for Y in Y1:
        for Z in Z1:
            print(X, Y, Z)
            left = not (X1 or Y1 or Z1)
            right = (not X1) and (not Y1) and (not Z1)

            print(left == right)
