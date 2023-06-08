# https://www.acmicpc.net/problem/1010

import sys

t = int(sys.stdin.readline().rstrip())

dp = [1, 1] + [0] * 29

for i in range(2, 31):
    dp[i] = dp[i-1] * i


for i in range(t):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    n = max(x, y)
    r = min(x, y)

    print(dp[n] // (dp[n-r] * dp[r]))
