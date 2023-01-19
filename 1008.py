# https://www.acmicpc.net/problem/1008

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print(round(a / b, 11))
