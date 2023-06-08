# https://www.acmicpc.net/problem/1449

import sys

n, l = map(int, sys.stdin.readline().rstrip().split())

problem = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

start = problem[0]
count = 0

while True:
    end = start + l - 1

    problem = list(filter(lambda x: x > end, problem))
    count += 1

    if len(problem) == 0:
        break
    else:
        start = problem[0]


print(count)
