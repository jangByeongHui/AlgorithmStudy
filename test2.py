import sys
import copy
from collections import deque

input = sys.stdin.readline

# init data
dice = [
    [-1, 2, -1],
    [4, 1, 3],
    [-1, 5, -1],
    [-1, 6, -1]
]
board = []

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 동쪽, 남쪽, 서쪽, 북쪽

# 데이터 입력
N, M, K = map(int, input().rstrip().split())

for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))


def rolling_dice(dice, dir):
    if dir == 0:  # 동쪽
        dice[3][1], dice[1][2], dice[1][1], dice[1][0] = dice[1][2], dice[1][1], dice[1][0], dice[3][1]
    elif dir == 1:  # 남쪽
        dice[3][1], dice[2][1], dice[1][1], dice[0][1] = dice[2][1], dice[1][1], dice[0][1], dice[3][1]
    elif dir == 2:  # 서쪽
        dice[3][1], dice[1][0], dice[1][1], dice[1][2] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
    else:  # 북쪽
        dice[3][1], dice[2][1], dice[1][1], dice[0][1] = dice[0][1], dice[3][1], dice[2][1], dice[1][1]


def calculate_point(x, y, board_dir):

    target_value = board[x][y]
    result = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque([(x, y)])

    point_direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:

        tx, ty = queue.popleft()
        if visited[tx][ty] == False:
            result += 1
            for dx, dy in point_direction:
                if 0 <= tx + dx < N and 0 <= ty + dy < M:
                    if board[tx+dx][ty+dy] == target_value:
                        queue.append((tx+dx,ty+dy))

            visited[tx][ty] = True #방문한 위치는 재방문 안함
        print("#######################")
        print(f'target_value :{target_value} tx: {tx} ty: {ty} tcount: {result} board_dir: {board_dir}')
        for row in visited:
            print(row)
        print("#######################\n")
    return result*target_value


board_dir = 0
x, y = 0, 0
point = 0
for index in range(K):


    dx, dy = direction[board_dir]

    x += dx
    y += dy
    rolling_dice(dice, board_dir)
    print(f"########### {index + 1} Rolling Dice############")
    for row in dice:
        print(row)
    print("##################################\n")
    print(f"dice[3][1]: {dice[3][1]},board_dir: {board_dir}")
    if 0 <= x < N and 0 <= y < N:
        if dice[3][1] > board[x][y]:
            board_dir = (board_dir + 1) % 4  # 다음 진행방향 90도 시계 방향으로 변환
            point += calculate_point(x, y, board_dir)
        elif dice[3][1] < board[x][y]:
            board_dir = board_dir - 1 if (board_dir - 1 < 0) else 0
            point += calculate_point(x, y, board_dir)
        else:
            point += calculate_point(x, y, board_dir)
    else:
        x -= 2 * dx
        y -= 2 * dy
        board_dir = (board_dir + 2) % 4  # 반대 방향으로 변환
        point += calculate_point(x, y, board_dir)

print(point)
