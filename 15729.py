# https://www.acmicpc.net/problem/15729

import sys

n = int(sys.stdin.readline().rstrip())
target = list(map(str, sys.stdin.readline().rstrip().split()))
text = ['0' for _ in range(n)]

count = 0

for i in range(n):
    if text[i] != target[i]:
        for j in range(i, i+3):
            if j >= len(text):
                break

            if text[j] == '1':
                text[j] = '0'
            else:
                text[j] = '1'

        count += 1

print(count)
