import sys
from itertools import product
from copy import deepcopy

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

office = []
cctv_list = {
    1:[[(0,1)],[(1,0)],[(0,-1)],[(-1,0)]],
    2:[[(0,1),(0,-1)],[(-1,0),(1,0)]],
    3:[[(-1,0),(0,1)],[(1,0),(0,1)],[(1,0),(0,-1)],[(-1,0),(0,-1)]],
    4:[[(0,-1),(1,0),(0,1)],[(1,0),(0,1),(0,-1)],[(-1,0),(1,0),(0,1)],[(-1,0),(0,-1),(1,0)]],
    5:[[(1,0),(0,1),(-1,0),(0,-1)]]
    }

for _ in range(N):
    office.append(list(map(int,input().rstrip().split())))

cctv_counter = []

for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv_counter.append((office[i][j],i,j))

answer = N*M

cctv_dir_ways = []

for cctv_num,x,y in cctv_counter:
    cctv_dir_ways.append(cctv_list[cctv_num])

def zero_counter(matrix,n,m):
    result = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                result += 1
    return result


for way in product(*cctv_dir_ways):
    temp_office = deepcopy(office)

    for index, directions in enumerate(way):
        _, x, y = cctv_counter[index]

        for dx, dy in directions:
            tx, ty = x + dx, y + dy

            while True:
                if 0 <= tx < N and 0 <= ty < M and temp_office[tx][ty] != 6:
                    temp_office[tx][ty] = "#"
                    tx += dx
                    ty += dy
                else:
                    break
    answer = min(answer,zero_counter(temp_office,N,M))

print(answer)