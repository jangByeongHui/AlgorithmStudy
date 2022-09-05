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

    print("########### temp board ############")
    for row in temp_board:
        print(row)
    print("###################################")

    # Up

    # #copy up board
    copy_up_board = []
    for row in temp_board:
        copy_up_board.append(row[:])
    for i in range(N):
        for j in range(N):
            if copy_up_board[i][j] != 0:
                current_row = i - 1
                while 0 <= current_row and copy_up_board[current_row][j] == 0:
                    current_row -= 1
                if 0 <= current_row and copy_up_board[current_row][j] == copy_up_board[i][j]:
                    copy_up_board[current_row][j] += copy_up_board[i][j]
                    copy_up_board[i][j] = 0
                elif 0 <= current_row != i-1:
                    copy_up_board[current_row+1][j] = copy_up_board[i][j]
                    copy_up_board[i][j] = 0
    queue.append((copy_up_board,count+1))

    # Down

    # copy down board
    copy_down_board = []
    for row in temp_board:
        copy_down_board.append(row[:])
    for i in range(N-1,-1,-1):
        for j in range(N):
            if copy_down_board[i][j] != 0:
                current_row = i + 1
                while current_row < N and copy_down_board[current_row][j] == 0:
                    current_row += 1
                if current_row  < N and copy_down_board[current_row][j] == copy_down_board[i][j]:
                    copy_down_board[current_row][j] += copy_down_board[i][j]
                    copy_down_board[i][j] = 0
                elif current_row < N and current_row != i+1:
                    copy_down_board[current_row-1][j] = copy_down_board[i][j]
                    copy_down_board[i][j] = 0
    queue.append((copy_down_board, count + 1))

    # Left
    # copy left board
    copy_left_board = []
    for row in temp_board:
        copy_left_board.append(row[:])

    for j in range(N):
        for i in range(N):
            if copy_left_board[i][j] != 0:
                current_col = j - 1
                while 0 <= current_col and copy_left_board[i][current_col] == 0:
                    current_col -= 1
                if 0 <= current_col and copy_left_board[i][current_col] == copy_left_board[i][j]:
                    copy_left_board[i][current_col] += copy_left_board[i][j]
                    copy_left_board[i][j] = 0
                elif 0 <= current_col and current_col != j-1:
                    copy_left_board[i][current_col+1] = copy_left_board[i][j]
                    copy_left_board[i][j] = 0
    queue.append((copy_left_board, count + 1))


    # # Right
    # # copy right board
    copy_right_board = []
    for row in temp_board:
        copy_right_board.append(row[:])

    for j in range(N-1,-1,-1):
        for i in range(N):
            if copy_right_board[i][j] != 0:
                current_col = j + 1
                while current_col < N and copy_right_board[i][current_col] == 0:
                    current_col += 1
                if current_col < N and copy_right_board[i][current_col] == copy_right_board[i][j] :
                    copy_right_board[i][current_col] += copy_right_board[i][j]
                    copy_right_board[i][j] = 0
                elif current_col < N and current_col != j + 1:
                    copy_right_board[i][current_col-1] = copy_right_board[i][j]
                    copy_right_board[i][j] = 0

    queue.append((copy_right_board, count + 1))

print(answer)





