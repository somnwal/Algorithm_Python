import sys

n = int(sys.stdin.readline().rstrip())

books = []

for i in range(n):
    books.append(int(sys.stdin.readline().rstrip()))

t = n
c = 0

for i in range(n-1, -1, -1):
    if books[i] == t:
        t -= 1
    else:
        c += 1

print(c)