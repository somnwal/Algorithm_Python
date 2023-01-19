# https://www.acmicpc.net/problem/1764

import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

arr = {}

for _ in range(n):
    key = sys.stdin.readline().rstrip()

    if key not in arr:
        arr[key] = 1
    else:
        arr[key] += 1

for _ in range(m):
    key = sys.stdin.readline().rstrip()

    if key not in arr:
        arr[key] = 1
    else:
        arr[key] += 1

arr = list(arr.items())
arr = list(filter(lambda x: x[1] > 1, arr))
arr = [ar[0] for ar in arr]

print(len(arr))
print('\n'.join(sorted(arr)))
