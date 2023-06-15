# https://www.acmicpc.net/problem/11724

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

mat = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
visit = [0 for _ in range(n + 1)]

arr = []

for i in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    mat[x][y] = 1
    mat[y][x] = 1


def bfs(v):
    q = [v]
    visit[v] = 1

    tmp = []

    while q:
        v = q.pop()
        tmp.append(v)

        for k in range(n + 1):
            if mat[v][k] == 1 and visit[k] == 0:
                q.append(k)
                visit[k] = 1

    return tmp


for i in range(1, n+1):
    if visit[i] == 0:
        arr.append(bfs(i))

print(len(arr))


