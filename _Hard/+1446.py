# https://www.acmicpc.net/problem/1446

import sys

l = 10001
n, d = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
dp = [i for i in range(l)]

arr.sort(key=lambda x: x[1])

for a in arr:
    dp[a[1]] = min(dp[a[0]] + a[2], dp[a[1]])

    for i in range(a[1] + 1, l):
        dp[i] = dp[i-1] + 1

print(dp[d])
