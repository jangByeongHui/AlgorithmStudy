import sys
from collections import deque

input = sys.stdin.readline

# input data
N, L, R = map(int,input().rstrip().split())

populations = []

for _ in range(N):
    populations.append(list(map(int,input().rstrip().split())))

# calculate
answer = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    union_set = []

    # 연합국가들 파악
    for i in range(N):
        for j in range(N):

            # 이미 다른 곳과 연합인 경우
            if visited[i][j]:
                continue
            queue = deque()
            union = []
            queue.append((i,j))

            while queue:
                x, y = queue.popleft()

                if visited[x][y]:
                    continue

                visited[x][y] = True
                union.append((x,y))

                for dx, dy in directions:
                    Dx ,Dy = x+dx,y+dy
                    if 0 <= Dx < N and 0 <= Dy < N and L<= abs(populations[x][y] - populations[Dx][Dy]) <= R and not visited[Dx][Dy]:
                        queue.append((Dx,Dy))
            union_set.append(union)

    if len(union_set) == N*N:
        break


    # 인구 이동 시작
    for countries in union_set:
        total_population = 0
        country_size = len(countries)

        for r, c in countries:
            total_population += populations[r][c]

        for r, c in countries:
            populations[r][c] = total_population//country_size

    answer += 1



print(answer)