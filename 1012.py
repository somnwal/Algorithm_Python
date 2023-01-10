# https://www.acmicpc.net/problem/1012
import sys

T = int(sys.stdin.readline().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = None
m = None
k = None
mat = None


def bfs(x, y):
    global mat

    q = [(x, y)]
    mat[x][y] = -1

    while q:
        (x, y) = q.pop(0)

        for idx in range(4):
            new_x = x + dx[idx]
            new_y = y + dy[idx]

            if 0 <= new_x < n:
                if 0 <= new_y < m:
                    if mat[new_x][new_y] == 1:
                        q.append((new_x, new_y))
                        mat[new_x][new_y] = -1


for _ in range(T):

    m, n, k = map(int, sys.stdin.readline().rstrip().split())

    mat = [[0 for _ in range(m)] for __ in range(n)]
    count = 0

    for i in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        mat[y][x] = 1

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                bfs(i, j)

                count += 1

    print(count)
