import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

city = []

for _ in range(N):
    city.append(list(map(int, input().rstrip().split())))

chicken = []
house = []

# 도시와 치킨집 위치 파악
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i,j))

# 치킨집 M개 선택
select_chicken = combinations(chicken,M)

answer = sys.maxsize
for way in select_chicken:
    result = 0
    for hx, hy in house:
        house_chicken_distance = sys.maxsize
        for cx,cy in way:
            house_chicken_distance = min(house_chicken_distance,abs(hx-cx)+abs(hy-cy))
        result += house_chicken_distance
    answer = min(answer,result)

print(answer)