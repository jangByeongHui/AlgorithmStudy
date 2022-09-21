import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

# 데이터 입력

N, M = map(int,input().rstrip().split())

research_center = []

for _ in range(N):
    research_center.append(list(map(int,input().rstrip().split())))


virus_pos = []
empty_space = 0
# 바이러스 놓을 수 있는 위치
for i in range(N):
    for j in range(N):
        if research_center[i][j] == 2:
            virus_pos.append((i,j))
        if research_center[i][j] == 0:
            empty_space += 1

answer = sys.maxsize

# virus 놓기
for selected_virus in combinations(virus_pos,M):
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(N)]
    copy_research_center = []
    spend_time = - sys.maxsize
    temp_empty_space = 0

    for row in research_center:
        copy_research_center.append(row[:])

    for virus in selected_virus:
        queue.append((virus[0],virus[1],0))

    while queue:

        x, y, seconds = queue.popleft()

        if visited[x][y]:
            continue

        if copy_research_center[x][y] == 0:
            temp_empty_space += 1
            copy_research_center[x][y] = 2

        spend_time = max(spend_time,seconds)
        if empty_space == temp_empty_space:
            break

        visited[x][y] = True

        for dx,dy in directions:
            temp_x,temp_y = x+dx,y+dy
            if 0 <= temp_x < N and 0 <= temp_y < N and not visited[temp_x][temp_y] and (copy_research_center[temp_x][temp_y] == 0 or copy_research_center[temp_x][temp_y] == 2): # 벽이 아니면 바이러스 전이
                queue.append((temp_x,temp_y,seconds+1))

    if empty_space == temp_empty_space:
        answer = min(answer,spend_time)


if answer == sys.maxsize:
    print(-1)
else:
    print(answer)