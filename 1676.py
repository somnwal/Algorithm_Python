# https://www.acmicpc.net/problem/1676

import sys

n = int(sys.stdin.readline().rstrip())

dp = [1, 1, 2]

for i in range(3, n+1):
    dp.append(dp[i-1] * i)

s = str(dp[n])
c = 0

while s[-1] == '0':
    c += 1
    s = s[:-1]

print(c)
