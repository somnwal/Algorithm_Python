# https://www.acmicpc.net/problem/1010

import sys, math

t = int(sys.stdin.readline().rstrip())

dp = [1, 1] + [0 for _ in range(29)]

for i in range(2, 31):
    dp[i] = dp[i-1] * i

for tt in range(t):
    a, b = map(int, sys.stdin.readline().rstrip().split())

    print(dp[b] // (dp[b-a] * dp[a]))
