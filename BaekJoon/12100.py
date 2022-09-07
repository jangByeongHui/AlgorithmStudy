import sys
from collections import deque
input = sys.stdin.readline

# input data
N = int(input().rstrip())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

answer = -sys.maxsize

# copy board
queue = deque()

temp_board = []
for row in board:
    temp_board.append(row[:])
queue.append((temp_board,0))

# calculate value
while queue:
    temp_board, count = queue.popleft()

    if count == 5:
        for row in temp_board:
            answer = max(answer,*row)
        continue
    # Up
    copy_up_board = []
    copy_up_board_visited =[[True for _ in range(N)] for _ in range(N)]
    for row in temp_board:
        copy_up_board.append(row[:])
    for i in range(N):
        for j in range(N):
            if copy_up_board[i][j] != 0:
                current_row = i - 1
                while 0 <= current_row and copy_up_board[current_row][j] == 0:
                    current_row -= 1
                if 0 <= current_row and copy_up_board_visited[current_row][j] and copy_up_board[current_row][j] == copy_up_board[i][j]:
                    copy_up_board[current_row][j] *= 2
                    copy_up_board[i][j] = 0
                    copy_up_board_visited[current_row][j] = False
                elif -1 <= current_row != i-1:
                    copy_up_board[current_row+1][j] = copy_up_board[i][j]
                    copy_up_board[i][j] = 0
    queue.append((copy_up_board,count+1))

    # Down
    copy_down_board = []
    copy_down_board_visited = [[True for _ in range(N)] for _ in range(N)]
    for row in temp_board:
        copy_down_board.append(row[:])
    for i in range(N-1,-1,-1):
        for j in range(N):
            if copy_down_board[i][j] != 0:
                current_row = i + 1
                while current_row < N and copy_down_board[current_row][j] == 0:
                    current_row += 1
                if current_row  < N and copy_down_board_visited[current_row][j] and copy_down_board[current_row][j] == copy_down_board[i][j]:
                    copy_down_board[current_row][j] *= 2
                    copy_down_board[i][j] = 0
                    copy_down_board_visited[current_row][j] = False
                elif current_row <= N and current_row != i+1:
                    copy_down_board[current_row-1][j] = copy_down_board[i][j]
                    copy_down_board[i][j] = 0
    queue.append((copy_down_board, count + 1))

    # Left
    copy_left_board = []
    copy_left_board_visited = [[True for _ in range(N)] for _ in range(N)]
    for row in temp_board:
        copy_left_board.append(row[:])

    for j in range(N):
        for i in range(N):
            if copy_left_board[i][j] != 0:
                current_col = j - 1
                while 0 <= current_col and copy_left_board[i][current_col] == 0:
                    current_col -= 1

                if 0 <= current_col and copy_left_board_visited[i][current_col] and copy_left_board[i][current_col] == copy_left_board[i][j]:
                    copy_left_board[i][current_col] *= 2
                    copy_left_board[i][j] = 0
                    copy_left_board_visited[i][current_col] = False
                elif -1 <= current_col and current_col != j-1:
                    copy_left_board[i][current_col+1] = copy_left_board[i][j]
                    copy_left_board[i][j] = 0
    queue.append((copy_left_board, count + 1))


    # Right
    copy_right_board = []
    copy_right_board_visited = [[True for _ in range(N)] for _ in range(N)]
    for row in temp_board:
        copy_right_board.append(row[:])

    for j in range(N-1,-1,-1):
        for i in range(N):
            if copy_right_board[i][j] != 0:
                current_col = j + 1
                while current_col < N and copy_right_board[i][current_col] == 0:
                    current_col += 1
                if current_col < N and copy_right_board_visited[i][current_col] and copy_right_board[i][current_col] == copy_right_board[i][j] :
                    copy_right_board[i][current_col] *= 2
                    copy_right_board[i][j] = 0
                    copy_right_board_visited[i][current_col] = False
                elif current_col <= N and current_col != j + 1:
                    copy_right_board[i][current_col-1] = copy_right_board[i][j]
                    copy_right_board[i][j] = 0
    queue.append((copy_right_board, count + 1))

print(answer)