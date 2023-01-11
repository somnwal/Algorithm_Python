# https://www.acmicpc.net/problem/2447

import sys

n = int(sys.stdin.readline().rstrip())

arr = [[' ' for _ in range(n+1)] for __ in range(n+1)]

def recur(i, j, level):
    level = int(level)

    if level == 1:
        arr[i][j] = '*'
        arr[i][j + 1] = '*'
        arr[i][j + 2] = '*'

        arr[i + 1][j] = '*'
        arr[i + 1][j + 2] = '*'

        arr[i + 2][j] = '*'
        arr[i + 2][j + 1] = '*'
        arr[i + 2][j + 2] = '*'
        return

    recur(i, j, level // 3)
    recur(i, j + (level * 1), level // 3)
    recur(i, j + (level * 2), level // 3)

    recur(i + (level * 1), j, level // 3)
    recur(i + (level * 1), j + (level * 2), level // 3)

    recur(i + (level * 2), j, level / 3)
    recur(i + (level * 2), j + (level * 1), level // 3)
    recur(i + (level * 2), j + (level * 2), level // 3)


recur(0, 0, n//3)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()
