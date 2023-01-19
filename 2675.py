# https://www.acmicpc.net/problem/2675

import sys

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    a = int(a)

    sys.stdout.write(''.join([bb * a for bb in b]) + '\n')
