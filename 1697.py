# https://www.acmicpc.net/problem/1697

import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

m = 100000

visit = [0 for _ in range(m+1)]


def bfs(v):
    q = [v]

    while q:
        v = q.pop(0)

        if v == k:
            print(visit[v])
            break

        for nx in (v-1, v+1, 2*v):
            if 0 <= nx <= m and not visit[nx]:
                visit[nx] = visit[v] + 1
                q.append(nx)


bfs(n)
