# https://www.acmicpc.net/problem/1495

import sys

n, s, m = map(int, sys.stdin.readline().rstrip().split())
v = list(map(int, sys.stdin.readline().rstrip().split()))


dp = [[0] * (m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if 0 <= j + v[i] <= m:
                dp[i+1][j + v[i]] = 1

            if 0 <= j - v[i] <= m:
                dp[i+1][j - v[i]] = 1

res = -1

for i in range(m+1):
    if dp[n][i] == 1:
        res = i

print(res)

