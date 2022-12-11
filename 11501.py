import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    s = list(map(int, sys.stdin.readline().rstrip().split()))

    sum = 0
    m = s[-1]

    for j in range(n-2, -1, -1):
        if s[j] > m:
            m = s[j]
        else:
            sum += (m - s[j])

    print(sum)