# https://www.acmicpc.net/problem/1309

import sys

n = int(sys.stdin.readline().rstrip())

dp = [1, 3, 7]

for i in range(3, 100001):
    dp.append(((dp[i-1] * 2) + dp[i-2]) % 9901)

print(dp[n])
