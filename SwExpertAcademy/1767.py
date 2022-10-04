from collections import deque

T = int(input())

directions = {"right":(0,1),"left":(0,-1),"down":(1,0),"up":(-1,0)}

def solution(index):

    # 데이터 입력
    N = int(input())
    maxinos = []
    cores = deque()
    max_core_count = 0
    min_wire_len = N*N
    base_core_count = 0

    for _ in range(N):
        maxinos.append(list(map(int,input().split())))

    # core 좌표 저장
    for i in range(N):
        for j in range(N):

            if maxinos[i][j] == 1 and (i == 0 or i == N-1 or j == 0 or j == N-1): # 최소 코어 갯수
                base_core_count += 1

            if maxinos[i][j] == 1:
                cores.append((i,j))

    # core 탐색 순서 변경
    cores_len = len(cores)
    for _ in range(cores_len):
        visited = [[False for _ in range(N)] for _ in range(N)]
        temp_max_core_count = base_core_count
        temp_min_wire_len = 0

        for x,y in cores:
            visited[x][y] = True

        for x,y in cores:
            if maxinos[x][y] == 1 and (x == 0 or x == N - 1 or y == 0 or y == N - 1):  # 이미 연결된 코어이므로 때문에 탐색 불필요
                continue
            queue = deque()
            queue.append((x, y, 'up'))
            queue.append((x, y, 'down'))
            queue.append((x, y, 'left'))
            queue.append((x, y, 'right'))

            while queue:
                tx, ty, tdir = queue.popleft()
                dx, dy = directions[tdir]

                if tx == 0 or tx == N-1 or ty == 0 or ty == N-1: # 먼저 찾은 최단 위치
                    vx, vy = x, y
                    vx += dx
                    vy += dy
                    temp_max_core_count += 1

                    while 0 <= vx < N and 0 <= vy < N:
                        temp_min_wire_len += 1 # 전선 길이 추가
                        visited[vx][vy] = True
                        vx += dx
                        vy += dy
                    break

                nx, ny = tx+dx, ty+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]: # 계속 갈 수 있거나 막힘이 없다면 계속 탐색
                    queue.append((nx,ny,tdir))

        # 정보 갱신
        if temp_max_core_count >= max_core_count:
            if temp_max_core_count == max_core_count:
                min_wire_len = min(min_wire_len,temp_min_wire_len)
            else:
                min_wire_len = temp_min_wire_len
            max_core_count = temp_max_core_count

        cores.appendleft(cores.pop()) # 왼쪽 방향으로 순서 변경

    print(f"#{index} {min_wire_len}")


for index in range(1,T+1):
    solution(index)