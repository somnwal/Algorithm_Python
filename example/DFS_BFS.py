import sys

n, l, v = map(int, sys.stdin.readline().rstrip().split(' '))

s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
visit = [0 for _ in range(n + 1)]


def dfs(v):
    print(v, end='')
    visit[v] = 1

    for i in range(n+1):
        for j in range(n+1):
            if visit[i] == 0 and s[v][i] == 1:
                dfs(i)


def bfs(v):
    q = [v]
    visit[v] = 0

    while q:
        v = q.pop(0)
        print(v, end='')

        for i in range(n + 1):
            for j in range(n + 1):
                if visit[i] == 1 and s[v][i] == 1:
                    q.append(i)
                    visit[i] = 0


for i in range(l):
    x, y = map(int, sys.stdin.readline().rstrip().split())

    s[x][y] = 1
    s[y][x] = 1


dfs(v)
print()
bfs(v)
