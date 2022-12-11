import sys

n = int(sys.stdin.readline().rstrip())

dist = list(map(int, sys.stdin.readline().rstrip().split()))
cost = list(map(int, sys.stdin.readline().rstrip().split()))

sum = 0
min_cost = cost[0]

for i in range(0, n-1):
    if cost[i] < min_cost:
        min_cost = cost[i]

    sum += (min_cost * dist[i])

print(sum)