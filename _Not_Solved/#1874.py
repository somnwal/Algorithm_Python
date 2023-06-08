# https://www.acmicpc.net/problem/1874

import sys

s = []
q = []
res = []

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    s.append(int(sys.stdin.readline().rstrip()))

cur = 2
q.append(1)
res.append('+')

while s and q:
    if cur >= n * n:
        res.clear()
        res.append('NO')
        break

    q.append(cur)
    res.append('+')

    if s[0] == q[-1]:
        res.append('-')
        s.pop(0)
        q.pop(-1)

        while (s and q) and (q[-1] == s[0]):
            res.append('-')
            s.pop(0)
            q.pop(-1)

    cur += 1

for r in res:
    print(r)
