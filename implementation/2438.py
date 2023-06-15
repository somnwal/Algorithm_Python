# https://www.acmicpc.net/problem/2438

import sys

n = int(sys.stdin.readline().rstrip())

for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()
