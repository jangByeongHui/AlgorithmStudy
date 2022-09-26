import sys
from collections import defaultdict, deque
from itertools import combinations

input = sys.stdin.readline

N = int(input().rstrip())
population = list(map(int,input().rstrip().split()))

graph = defaultdict(list)
answer = sys.maxsize

def bfs(area):

    visited = [False] * N

    queue = deque([area[0]])
    visited[area[0]] = True

    while queue:
        node = queue.popleft()

        for near_node in graph[node]:
            if not visited[near_node] and near_node in area:
                queue.append(near_node)
                visited[near_node] = True

    # 리스트에 포함된 모든 노드를 순회 가능한지
    for node_index in area:
        if visited[node_index] != True:
            return False
    else:
        return True


# 노드 간에 연결 확인하기
for index in range(N):
    row = list(map(int, input().rstrip().split()))
    for row_index in range(row[0]):
        graph[index].append(row[row_index+1]-1)

# 두 구역으로 나누기
for way in range(1,N//2+1):

    for group_1 in combinations(range(N),way):
        group_2 = [element for element in range(N) if element not in group_1]

        # 연결된 노드인지 확인

        if bfs(group_1) and bfs(group_2):
            sum_1 = 0

            for g1 in group_1:
                sum_1 += population[g1]

            sum_2 = 0
            for g2 in group_2:
                sum_2 += population[g2]

            answer = min(answer,abs(sum_1-sum_2))

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)