import sys
from copy import deepcopy

input = sys.stdin.readline

directions = [(-1,0),(1,0),(0,-1),(0,1)]

cctv_directions = [
    [[0],[1],[2],[3]]
    ,[[0,1],[2,3]]
    ,[[0,2],[0,3],[1,2],[1,3]]
    ,[[0,1,2],[0,1,3],[0,2,3],[1,2,3]]
    ,[[0,1,2,3]]
]

office = []
cctv_list = []


N, M = map(int,input().rstrip().split())

# 데이터 입력
for x in range(N):
    row = list(map(int,input().rstrip().split()))
    office.append(row)
    for y, element in enumerate(row):
        if 1 <= element <= 5:
            cctv_list.append((x,y,element))

# 재귀 탐색 함수 정의
cctv_list_len = len(cctv_list)
answer = N*M

def fill_cctv_area(x,y,direction,matrix):


    for dir_num in direction:

        nx, ny = x, y
        dx, dy = directions[dir_num]

        while True:

            nx += dx
            ny += dy

            if not (0 <= nx < N and 0 <= ny < M):
                break

            if matrix[nx][ny] == 6:
                break

            if matrix[nx][ny] == 0:
                matrix[nx][ny] = "#"

def dfs(depth,matrix):
    global answer

    if depth == cctv_list_len:
        count = 0
        for row in matrix:
            count += row.count(0)
        answer = min(answer,count)
        return

    x, y , cctv_type = cctv_list[depth]
    temp_matrix = deepcopy(matrix) # 이전 상태로 복귀

    for dir in cctv_directions[cctv_type-1]:
        fill_cctv_area(x,y,dir,temp_matrix)
        dfs(depth+1,temp_matrix)
        temp_matrix = deepcopy(matrix)

dfs(0,office)

print(answer)