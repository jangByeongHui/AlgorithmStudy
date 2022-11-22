import sys
from collections import deque

r, c = map(int, sys.stdin.readline().rsplit())
visited = [[False for _ in range(c)] for _ in range(r)]
arr = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(r)]
answer = [[0 for _ in range(c)] for _ in range(r)]
d = ((0, 1), (0, -1), (1, 0), (-1, 0))

for i in range(r):
    for j in range(c):
        if arr[i][j] == 1: answer[i][j] = 1


def bfs(sy, sx):
    q = deque()
    q.append((sy, sx))
    cnt = 1
    ones = []

    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]

            if -1 < ny < r and -1 < nx < c:
                if visited[ny][nx]: continue
                visited[ny][nx] = True

                if arr[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1

                else:
                    ones.append((ny, nx))

    for y, x in ones:
        visited[y][x] = False
        answer[y][x] += cnt
        if answer[y][x] >= 10: answer[y][x] %= 10


for i in range(r):
    for j in range(c):
        if arr[i][j] == 0:
            if not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)

for i in range(r):
    print(''.join(map(str, answer[i])))