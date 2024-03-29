# https://www.acmicpc.net/problem/1106

import sys

INF = 1e9

c, n = map(int, sys.stdin.readline().rstrip().split())
data = []

min_cost = [INF] * (c+100)
min_cost[0] = 0

for _ in range(n):
    # cost, cus
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

# cost 작은 순서로 정리
data_sort = sorted(data, key = lambda x: x[0])

for cost, cus in data_sort:
    for i in range(cus, c+100):
        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])

print(min(min_cost[c:]))
