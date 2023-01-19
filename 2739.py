# https://www.acmicpc.net/problem/2739

import sys

n = int(sys.stdin.readline().rstrip())

print('\n'.join([f'{n} * {i} = {n * i}' for i in range(1, 10)]))
