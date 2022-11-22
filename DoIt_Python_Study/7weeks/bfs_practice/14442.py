import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(start,K):
    visited = [[[-1] * C for _ in range(R)] for _ in range(K+1)]
    queue = deque()
    queue.append([0] + start)
    answer = R+C+1
    visited[0][start[0]][start[1]] = 0
    while queue:
        break_cnt, x, y = queue.popleft()
        if x == R-1 and y == C-1:
            return visited[break_cnt][x][y]+1
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < R and 0 <= ay < C:
                if board[ax][ay] == 1 and break_cnt < K and visited[break_cnt + 1][ax][ay] == -1 :
                    queue.append([break_cnt+1,ax,ay])
                    visited[break_cnt+1][ax][ay] = visited[break_cnt][x][y] + 1
                elif board[ax][ay] == 0 and visited[break_cnt][ax][ay] == -1:
                    queue.append([break_cnt,ax,ay])
                    visited[break_cnt][ax][ay] = visited[break_cnt][x][y] + 1
    return -1
R,C,K = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(R)]

print(bfs([0,0],K))