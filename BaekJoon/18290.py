import sys
from itertools import combinations

N, M, K = map(int,input().split())
position_list = []
directions = [(0,1),(1,0),(-1,0),(0,-1)]

board = []

for _ in range(N):
    board.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        position_list.append((i,j))


answer = -sys.maxsize

for way in combinations(position_list,K):

    visited = [[False for _ in range(M)] for _ in range(N)]

    for x, y in way:
        visited[x][y] = True

    unavailable = False
    result = 0
    for x, y in way:

        if unavailable:
            break
        result += board[x][y]
        for dx, dy in directions:
            new_x, new_y = x+dx, y+dy

            if 0 <= new_x < N and 0 <= new_y < M and visited[new_x][new_y]:
                unavailable = True
                break
    else:
        answer = max(result,answer)

print(answer)