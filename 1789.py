import sys

num = int(sys.stdin.readline().rstrip())

a = 1
s = 0
c = 0

while True:
    s += a
    a += 1
    c += 1

    if s > num:
        c -= 1
        break

print(c)