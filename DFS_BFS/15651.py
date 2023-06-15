# https://www.acmicpc.net/problem/15651

import sys

arr = []


def dfs(tmp):
    if len(tmp) == m:
        arr.append(' '.join(tmp))
        return

    for i in range(1, n + 1):
        new_tmp = tmp[:]
        new_tmp.append(str(i))

        dfs(new_tmp)


n, m = map(int, sys.stdin.readline().rstrip().split())

dfs([])

arr.sort()

for a in arr:
    print(a)
