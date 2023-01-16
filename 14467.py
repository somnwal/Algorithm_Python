# https://www.acmicpc.net/problem/14467

import sys

n = int(sys.stdin.readline().rstrip())

arr = {}
count = [0 for i in range(11)]

for i in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    if x not in arr:
        arr[x] = y
    else:
        if y != arr[x]:
            arr[x] = y
            count[x] += 1

print(sum(count))
