# https://www.acmicpc.net/problem/6571

import sys

arr = [0, 1, 2] + [0] * 600

p = []

# 피보나치 구하기
for i in range(3, len(arr)):
    arr[i] = arr[i - 2] + arr[i - 1]

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == 0 and b == 0:
        break

    p.append([a, b])

    count = 0

    for i in range(1, len(arr)):
        if a <= arr[i] <= b:
            count += 1

    print(count)
