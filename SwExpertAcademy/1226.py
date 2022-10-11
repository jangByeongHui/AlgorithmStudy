from collections import deque

directions = [(0,1),(1,0),(0,-1),(-1,0)]

for _ in range(10):
    T = int(input())
    answer = 0
    miro = [[1 for _ in range(16)] for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    queue = deque([])

    for i in range(16):
        row = input()
        for j,element in enumerate(row):
            miro[i][j] = int(element)
            if int(element) == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True

        if miro[x][y] == 3:
            answer = 1
            break

        for dx, dy in directions:
            nx, ny = x+dx, y+dy

            if 0 <= nx < 16 and 0 <= ny < 16 and visited[nx][ny] == False and miro[nx][ny] != 1:
                queue.append((nx,ny))
    print(f"#{T} {answer}")