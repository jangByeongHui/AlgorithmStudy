from collections import deque
from copy import deepcopy

# 데이터 입력
n, m, q = map(int, input().split())

disks = []

for _ in range(n):
    disks.append(deque(list(map(int, input().split()))))


def rotate_disk(x, d, k):
    for i in range(n):
        if (i + 1) % x != 0:
            continue
        for _ in range(k):
            if d == 0:
                disks[i].appendleft(disks[i].pop())
            else:
                disks[i].append(disks[i].popleft())


directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def calculate_near_number():
    # 숫자별로 인접한 숫자들 찾은 후 삭제
    for i in range(n):
        for j in range(m):

            # 없는 숫자임으로 생략
            if disks[i][j] == 0:
                continue
            visited = [[False for _ in range(m)] for _ in range(n)]
            queue = deque([(i, j)])
            delete_candidate = []

            # 인접한 숫자들 전부 찾기
            while queue:
                x, y = queue.pop()

                if visited[x][y]:
                    continue
                visited[x][y] = True
                delete_candidate.append((x, y))

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if ny == m:
                        ny = 0
                    if ny == -1:
                        ny = m-1

                    if 0 <= nx < n and 0 <= ny < m and disks[i][j] == disks[nx][ny] and not visited[nx][ny]:
                        queue.append((nx, ny))

            # 인접한 숫자가 자신 이외에 존재
            if len(delete_candidate) > 1:
                for x, y in delete_candidate:
                    disks[x][y] = 0


def regulation_disk():
    element_sum = 0
    element_count = 0
    for i in range(n):
        for j in range(m):
            if disks[i][j] != 0:
                element_sum += disks[i][j]
                element_count += 1

    if element_count == 0:
        return False
    element_avg = element_sum / element_count

    for i in range(n):
        for j in range(m):
            if disks[i][j] == 0:
                continue
            if disks[i][j] > element_avg:
                disks[i][j] -= 1
            elif disks[i][j] < element_avg:
                disks[i][j] += 1
    return True
for _ in range(q):
    x, d, k = map(int, input().split())

    rotate_disk(x, d, k)
    temp_disk = deepcopy(disks)
    calculate_near_number()

    for i in range(n):
        if disks[i] != temp_disk[i]:
            break
    else:
        if not regulation_disk():
            break

answer = 0

for row in disks:
    answer += sum(row)

print(answer)