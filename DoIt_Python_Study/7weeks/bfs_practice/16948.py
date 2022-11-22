import sys
from collections import deque


# bfs 탐색
def bfs():
    queue = deque()
    queue.append([r1, c1])
    visited[r1][c1] = 1

    while queue:
        a, b = queue.popleft()

        # 6가지 이동 방법을 확인한다.
        for i in range(6):
            x = a + dx[i]
            y = b + dy[i]

            # 범위 내에 있고 탐색하지 않았다면 탐색한다.
            if 0 <= x < n and 0 <= y < n and visited[x][y] == 0:
                # 탐색하기까지 걸린 이동 횟수를 초기화
                visited[x][y] = visited[a][b] + 1
                queue.append((x, y))


n = int(sys.stdin.readline())

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

# 각 좌표까지 가기 위한 이동 횟수 체크
visited = [[0] * n for _ in range(n)]

bfs()

# 목표 좌표까지 이동한 횟수에서
# 처음 시작 좌표에서 카운트한 값을 빼준다.
print(visited[r2][c2] - 1)