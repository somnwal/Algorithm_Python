# https://www.acmicpc.net/problem/1904

import sys

n = int(sys.stdin.readline().rstrip())

dp = [0, 1, 2, 3, 5]

for i in range(5, n+1):
    dp.append((dp[i-2] + dp[i-1]) % 15746)

print(dp[n])
