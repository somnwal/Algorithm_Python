# https://www.acmicpc.net/problem/1931

import sys

n = int(sys.stdin.readline().rstrip())

t = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    t.append([a, b])

t = sorted(t, key=lambda x: (x[1], x[0]))

l = 0
c = 0

for i, j in t:
    if i >= l:
        c += 1
        l = j


print(c)
