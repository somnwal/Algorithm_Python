#https://www.acmicpc.net/problem/10997

import sys

#n = int(sys.stdin.readline().rstrip())
n = 2
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
arr = [[0 for _ in range(2*)] for __ in range(n)]

target = (int(n//2), (n//2))

prev = None

i = 0
j = n-1

print(target)