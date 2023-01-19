# https://www.acmicpc.net/problem/2562

import sys

arr = [int(sys.stdin.readline().rstrip()) for _ in range(9)]

sys.stdout.write(str(max(arr)) + '\n')
sys.stdout.write(str(arr.index(max(arr)) + 1) + '\n')
