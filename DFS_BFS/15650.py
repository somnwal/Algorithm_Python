# https://www.acmicpc.net/problem/15650

import sys

arr = []


def dfs(tmp, prev):
    if len(tmp) == m:
        arr.append(' '.join(tmp))
        return

    for i in range(1, n+1):
        new_tmp = tmp[:]
        new_tmp.append(str(i))

        if i > prev:
            dfs(new_tmp, i)


n, m = map(int, sys.stdin.readline().rstrip().split())

dfs([], 0)

arr.sort()

for a in arr:
    print(a)
