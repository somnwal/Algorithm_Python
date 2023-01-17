# https://www.acmicpc.net/problem/9461

import sys

dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90

for i in range(10, len(dp)):
    dp[i] = dp[i-2] + dp[i-3]

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    print(dp[int(sys.stdin.readline().rstrip()) - 1])
