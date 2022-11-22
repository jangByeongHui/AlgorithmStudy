import sys
from collections import deque

scan = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]
shark_size = 2
max_int  = 20
max_val = 401

min_dist = max_val
min_x = max_int
min_y = max_int

queue = deque([])
shark = []
check = []


N = int(scan())

for _ in range(N):
    shark.append(list(map(int,scan().rstrip().split())))
    check.append([-1]*N)

for i in range(N):
    for j in range(N):
        if shark[i][j] == 9:
            shark_x = i
            shark_y = j
            shark[i][j] = 0

def BFS(X,Y):
    global min_dist, min_x, min_y, check, N
    check[X][Y] = 0
    queue.append((X,Y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx > N-1 or ny < 0 or ny > N-1: continue
            # print(nx,ny)
            if check[nx][ny] != -1 or shark[nx][ny] > shark_size: continue

            check[nx][ny] = check[x][y] + 1

            if shark[nx][ny] != 0 and shark[nx][ny] < shark_size:
                if min_dist > check[nx][ny]:
                    min_x = nx
                    min_y = ny
                    min_dist = check[nx][ny]

                elif min_dist == check[nx][ny]:
                    if min_x == nx:
                        if min_y > ny:
                            min_x = nx
                            min_y = ny
                    elif min_x > nx:
                        min_x = nx
                        min_y = ny
            queue.append((nx,ny))

result = 0
eat_cnt = 0

while True:
    min_dist = max_val
    min_x = max_int
    min_y = max_int

    for i in range(N):
        for j in range(N):
            check[i][j] = -1

    BFS(shark_x,shark_y)
    if min_x != max_int and min_y != max_int:
        result += check[min_x][min_y]
        eat_cnt += 1

        if eat_cnt == shark_size:
            shark_size += 1
            eat_cnt =0

        shark[min_x][min_y] = 0

        shark_x = min_x
        shark_y = min_y

    else:
        break

print(result)


