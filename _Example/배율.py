n = [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.02]

for nn in n:
    for i in range(2, 31):
        print(nn, '^', i, '=', round(nn ** i, 2), '배')
    print()
