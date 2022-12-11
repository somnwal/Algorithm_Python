import sys

a, b = map(int, sys.stdin.readline().rstrip().split(" "))

r = 1

while b != a:
    r += 1
    temp = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2

    if temp == b:
        print(-1)
        break
else:
    print(r)
