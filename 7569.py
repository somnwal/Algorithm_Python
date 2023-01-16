# https://www.acmicpc.net/problem/7569

import sys

m, n, h = map(int, sys.stdin.readline().rstrip().split())

arr = [[[-1 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
q = []
dx = [-1, 1]

count = 0
s = 0

for i in range(h):
    for j in range(n):
        l = list(map(int, sys.stdin.readline().rstrip().split()))

        for k in range(m):
            if l[k] == 1:
                q.append((i, j, k))
                s += 1

            arr[i][j][k] = l[k]

if s == (n*m*h):
    print(0)
else:
    while q:
        qq = q[:]
        q = []
        for v in qq:
            for i in range(2):
                di = v[0] + dx[i]
                if di < 0 or di >= h:
                    continue
                if arr[di][v[1]][v[2]] == 0:
                    arr[di][v[1]][v[2]] = 1
                    s += 1
                    q.append((di, v[1], v[2]))

            for j in range(2):
                dj = v[1] + dx[j]
                if dj < 0 or dj >= n:
                    continue
                if arr[v[0]][dj][v[2]] == 0:
                    arr[v[0]][dj][v[2]] = 1
                    s += 1
                    q.append((v[0], dj, v[2]))

            for k in range(2):
                dk = v[2] + dx[k]
                if dk < 0 or dk >= m:
                    continue
                if arr[v[0]][v[1]][dk] == 0:
                    arr[v[0]][v[1]][dk] = 1
                    s += 1
                    q.append((v[0], v[1], dk))
        count += 1
    count -= 1

    for a in arr:
        for b in a:
            if 0 in b:
                count = -1
                break

    print(count)




