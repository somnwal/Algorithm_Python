m = 100000

prime = [False, False] + [True] * (m-2)

for i in range(2, int(m ** 0.5) + 1):
    if prime[i]:
        for j in range(i+i, m, i):
            if prime[j]:
                prime[j] = False

print(prime[37])
print(prime[21])