import sys
input = sys.stdin.readline

N, L, R = map(int,input().rstrip().split())

population = []
directions = [(1,0),(-1,0),(0,1),(0,-1)]
answer = 0
for _ in range(N):
    population.append(list(map(int,input().rstrip().split())))

while True:
    visited = [[True for _ in range(N)] for _ in range(N) ]
    changed_population = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                stack = [(i,j)]
                union_country = [(i,j)]
                union_sum = population[i][j]
                union_count = 1

                while stack:
                    x, y = stack.pop()
                    visited[x][y] = False

                    for dx, dy in directions:
                        if 0 <= x+dx < N and 0 <= y+dy < N and visited[x+dx][y+dy] and L <= abs(population[x][y] - population[x+dx][y+dy]) <= R:
                            union_sum += population[x+dx][y+dy]
                            union_count += 1
                            union_country.append((x+dx,y+dy))
                            stack.append((x+dx,y+dy))

                union_avg = union_sum//union_count
                for (x,y) in union_country:
                    changed_population[x][y] = union_avg
    for i in range(N):
        if population[i] != changed_population[i]:
            break
    else:
        break

    for i in range(N):
        for j in range(N):
            population[i][j] = changed_population[i][j]
    answer += 1

print(answer)