import sys

t = int(sys.stdin.readline().rstrip())

a = 0
b = 0
c = 0

if t % 10 != 0:
    print(-1)
else:
    a += t//300
    t -= 300 * (t//300)

    b += t//60
    t -= 60 * (t//60)

    c += t//10
    t -= 10 * (t//10)

    print(f"{a} {b} {c}")
