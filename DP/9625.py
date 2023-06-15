# https://www.acmicpc.net/problem/9625

import sys

a = [1, 0, 1, 1] + [0] * 42
b = [0, 1, 1, 2] + [0] * 42

for i in range(4, 46):
    a[i] = a[i-2] + a[i-1]
    b[i] = b[i-2] + b[i-1]

k = int(sys.stdin.readline().rstrip())
print(a[k], b[k])