from collections import deque

directions = [(0,-1),(0,1),(1,0)]

for _ in range(10):
    index = int(input())
    answer = -1

    ladder = []

    for _ in range(100):
        ladder.append(list(map(int,input().split())))

    for start in range(100):
        visited = [[False for _ in range(100)] for _ in range(100)]

        if ladder[0][start] == 1:
            queue = deque([(0,start)])

            while queue:

                x, y = queue.pop()

                if visited[x][y]:
                    continue
                visited[x][y] = True

                if ladder[x][y] == 2: # X 위치를 찾음
                    answer = start
                    break

                for dx, dy in directions:
                    tx, ty = x+dx, y+dy

                    if 0 <= tx < 100 and 0 <= ty < 100 and ladder[tx][ty] != 0 and not visited[tx][ty]:
                        queue.append((tx,ty))
                        break
    print(f"#{index} {answer}")