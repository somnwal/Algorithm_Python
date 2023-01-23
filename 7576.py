# https://www.acmicpc.net/problem/7576

import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

print(arr)
