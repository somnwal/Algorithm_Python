# https://www.acmicpc.net/problem/1330

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

print('==' if a == b else ('<' if a < b else '>'))
