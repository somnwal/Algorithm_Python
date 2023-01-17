# https://www.acmicpc.net/problem/2579

import sys

n = int(sys.stdin.readline().rstrip())

s = [0 for i in range(301)]
dp = [0 for j in range(301)]

for i in range(n):
    s[i] = int(sys.stdin.readline().rstrip())

dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])

print(dp[n - 1])
