# https://www.acmicpc.net/problem/14468

import sys

arr = {}
count = 0

s = list(sys.stdin.readline().rstrip())

for i in range(26):
    a = chr(i+65)

    tmp = list(filter(lambda e: s[e] == a, range(len(s))))
    arr[a] = (tmp[0], tmp[1])

for i in range(26):
    for j in range(i+1, 26):
        a = chr(i+65)
        b = chr(j+65)

        s1 = arr[a][0]
        s2 = arr[a][1]
        e1 = arr[b][0]
        e2 = arr[b][1]

        if (s1 < e1) and (e1 < s2) and (s2 < e2):
            count += 1
        elif (e1 < s1) and (s1 < e2) and (e2 < s2):
            count += 1

print(count)
