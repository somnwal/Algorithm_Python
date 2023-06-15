# https://www.acmicpc.net/problem/9465

import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())

    dp = []
    max_list = []
    s = 0

    for i in range(2):
        tmp = list(map(int, sys.stdin.readline().rstrip().split()))
        dp.append(tmp)

        for j in range(len(tmp)):
            max_list.append([tmp[j], [i, j]])

    max_list.sort(key=lambda x: -x[0])

    for i in range(len(max_list)):
        max_one = max_list[i]

        ti = max_one[1][0]
        tj = max_one[1][1]
        tn = dp[ti][tj]

        if tn == 0:
            continue

        s += tn

        for di in [-1, 1]:
            new_i = ti + di
            if 0 <= new_i <= 1:
                dp[new_i][tj] = 0
        for dj in [-1, 1]:
            new_j = tj + dj
            if 0 <= new_j <= n-1:
                dp[ti][new_j] = 0

    print(s)


