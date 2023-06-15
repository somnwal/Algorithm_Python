# https://www.acmicpc.net/problem/7576

import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

d = [-1, 1]
arr = [[-1 for _ in range(m)] for __ in range(n)]

day = 0
s = 0

q = []

for i in range(n):
    l = list(map(int, sys.stdin.readline().rstrip().split()))

    for j in range(m):
        if l[j] == 1:
            s += 1
            q.append((i, j))
        arr[i][j] = l[j]

if s == (n * m):
    print(0)
else:
    while q:
        qq = q[:]
        q = []

        for v in qq:
            for i in range(2):
                dx = v[0] + d[i]
                if dx < 0 or dx > n-1:
                    continue
                if arr[dx][v[1]] == 0:
                    arr[dx][v[1]] = 1
                    s += 1
                    q.append((dx, v[1]))
            for i in range(2):
                dy = v[1] + d[i]
                if dy < 0 or dy > m-1:
                    continue
                if arr[v[0]][dy] == 0:
                    arr[v[0]][dy] = 1
                    s += 1
                    q.append((v[0], dy))
        day += 1
    day -= 1

    for a in arr:
        if 0 in a:
            day = -1
            break

    print(day)
