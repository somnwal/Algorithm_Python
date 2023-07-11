# https://www.acmicpc.net/problem/5014

import sys

sys.setrecursionlimit(100000000)

f, s, g, u, d = map(int, sys.stdin.readline().rstrip().split())

cost = [1000000 for _ in range(f+1)]

res = []


def dfs(v, c):
    if v < 1 or v > f:
        return

    if v == g:
        res.append(c)
        return

    if cost[v] > c:
        cost[v] = c
    else:
        return

    if v + u <= f:
        dfs(v + u, c+1)
    if v - d >= 0:
        dfs(v - d, c+1)


dfs(s, 0)


if len(res) > 0:
    print(min(res))
else:
    print('use the stairs')
