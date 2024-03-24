# https://www.acmicpc.net/problem/1439

import sys

input = sys.stdin.readline

s = input().rstrip()

zc = sum(len(i) != 0 for i in s.split("1"))
oc = sum(len(i) != 0 for i in s.split("0"))

print(min(zc, oc))