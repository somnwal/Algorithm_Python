# https://www.acmicpc.net/problem/2133

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0, 0, 2] + [0] * 28

1 0
2 3
3 0
4 9

for i in range(31):
    dp[i] = dp[dp[i] // 3]