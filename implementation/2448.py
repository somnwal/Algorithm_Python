# https://www.acmicpc.net/problem/2448

import sys

n = int(sys.stdin.readline().rstrip())
arr_i = [3 * (2**k) for k in range(12)]

s = arr_i[arr_i.index(n) + 1]

arr = [[' ' for _ in range(s)] for __ in range(n)]


def rec(i, j, l):
    if i < 0 or j >= s:
        return

    if l == 0:
        arr[i][j:j+4] = ['*', '*', '*', '*', '*']
        arr[i - 1][j + 1] = '*'
        arr[i - 1][j + 3] = '*'
        arr[i - 2][j + 2] = '*'
        return

    o = arr_i[l]
    o2 = arr_i[l-1]

    rec(i, j + (o * 0), l - 1)
    rec(i, j + (o * 1), l - 1)
    rec(i - (o2 * 1), j + (o2 * 1), l - 1)


rec(n-1, 0, arr_i.index(n))

for i in range(n):
    for j in range(s-1):
        sys.stdout.write('%s' % arr[i][j])
    sys.stdout.write('\n')
