# https://www.acmicpc.net/problem/1541

import sys

line = sys.stdin.readline().rstrip()
lines = line.split("-")

is_first = True
sum = 0

for l in lines:
    tmp_l = l.split("+")
    tmp_s = 0

    for tmp_tmp_l in tmp_l:
        tmp_s += int(tmp_tmp_l)

    if is_first:
        sum += tmp_s
        is_first = False
    else:
        sum -= tmp_s

print(sum)
