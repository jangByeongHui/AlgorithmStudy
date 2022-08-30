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
    temp_dice = copy.deepcopy(dice)

    target_value = board[x][y]
    result = -sys.maxsize
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue = deque([(x, y, 1)])
    temp_board_dir = board_dir
    print(target_value)
    while queue:

        tx, ty, tcount = queue.popleft()
        result = max(result,tcount)
        print("########################\n")
        print(temp_dice[3][1], temp_board_dir)
        for row in visited:
            print(row)
        print("########################\n")

        if visited[tx][ty] == False:
            rolling_dice(temp_dice, temp_board_dir)
            dx, dy = direction[temp_board_dir]

            if 0 <= tx + dx < N and 0 <= ty + dy < M:
                if board[tx+dx][ty+dy] == target_value:
                    queue.append((tx+dx,ty+dy,tcount+1))
                else:
                    queue.append((tx + dx, ty + dy, 0))

                if temp_dice[3][1] > board[tx+dx][ty+dy]:
                    temp_board_dir = (temp_board_dir + 1) % 4  # 다음 진행방향 90도 시계 방향으로 변환
                elif temp_dice[3][1] < board[tx+dx][ty+dy]:
                    temp_board_dir = temp_board_dir - 1 if (temp_board_dir - 1 < 0) else 0
            else:
                if board[tx-dx][ty-dy] == target_value:
                    queue.append((tx-dx,ty-dy,tcount+1))
                else:
                    queue.append((tx - dx, ty - dy, 0))
                temp_board_dir = (temp_board_dir + 2) % 4  # 반대 방향으로 변환

            visited[tx][ty] = True #방문한 위치는 재방문 안함
    return result*target_value


board_dir = 0
x, y = 0, 0
point = 0
for _ in range(K):
    rolling_dice(dice, board_dir)
    print("###########Rolling Dice############")
    for row in dice:
        print(row)
    print("##################################\n")

    dx, dy = direction[board_dir]

    x += dx
    y += dy

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
        y -= 2 * dx
        board_dir = (board_dir + 2) % 4  # 반대 방향으로 변환
        point += calculate_point(x, y, board_dir)

print(point)