import sys
from itertools import combinations

input = sys.stdin.readline

directions = [(1,0),(-1,0),(0,1),(0,-1)]

# 데이터 입력
N, M = map(int, input().rstrip().split())

research_center = []

for _ in range(N):
    research_center.append(list(map(int, input().rstrip().split())))

def spread_virus(N, M, matrix):
    temp_matrix = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    for row in matrix:
        temp_matrix.append(row[:])

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if temp_matrix[i][j] == 2:
                stack = [(i,j)]

                while stack:
                    x, y = stack.pop()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    temp_matrix[x][y] = 2 # 바이러스 전이

                    # 상하좌우 확산
                    for dx, dy in directions:
                        Dx, Dy = x+dx, y+dy

                        if 0 <= Dx < N and 0 <= Dy < M:
                            if temp_matrix[Dx][Dy] == 0:
                                stack.append((Dx,Dy))

    result = 0
    for i in range(N):
        for j in range(M):
            if temp_matrix[i][j] == 0:
                result += 1
    return result

def build_wall_and_caclculate(N,M,research_center):

    safe_point = []
    answer = - sys.maxsize

    for i in range(N):
        for j in range(M):
            if research_center[i][j] == 0:
                safe_point.append((i,j))

    for way in combinations(safe_point,3):
        temp_research_center = []

        for row in research_center:
            temp_research_center.append(row[:])

        for x, y in way:
            temp_research_center[x][y] = 1

        answer = max(answer,spread_virus(N,M,temp_research_center))

    return answer

print(build_wall_and_caclculate(N,M,research_center))