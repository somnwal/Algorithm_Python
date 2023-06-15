# https://www.acmicpc.net/problem/14888

import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))
init_op = list(map(int, sys.stdin.readline().rstrip().split()))

arr = []


def dfs_max(op, cur, i):
    if i == len(numbers):
        arr.append(cur)
        return

    for j in range(4):
        if op[j] == 0:
            continue

        new_op = op[:]
        new_op[j] -= 1

        if j == 0:
            dfs_max(new_op, cur + numbers[i], i + 1)
        elif j == 1:
            dfs_max(new_op, cur - numbers[i], i + 1)
        elif j == 2:
            dfs_max(new_op, cur * numbers[i], i + 1)
        elif j == 3:
            new_cur = cur

            if cur < 0:
                new_cur = cur * -1
                new_cur = new_cur // numbers[i]
                new_cur = new_cur * -1
            else:
                new_cur = new_cur // numbers[i]

            dfs_max(new_op, new_cur, i + 1)


dfs_max(init_op, numbers[0], 1)

print(max(arr))
print(min(arr))
