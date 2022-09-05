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

for i in range(1):
    temp_board = []
    for row in board:
        temp_board.append(row[:])
    queue.append((temp_board,0))

# calculate value
while queue:
    temp_board, count = queue.popleft()

    if count >= 5:
        for row in temp_board:
            answer = max(answer,*row)
        break


    # Up

    #copy up board
    copy_up_board = []
    for row in temp_board:
        copy_up_board.append(row)
    for i in range(N):
        for j in range(N):


    queue.append((copy_up_board,count+1))

    # Down

    # copy down board
    copy_down_board = []
    for row in temp_board:
        copy_down_board.append(row)
    for i in range(N):
        for j in range(N):


    queue.append((copy_down_board, count + 1))

    # Left
    # copy left board
    copy_left_board = []
    for row in temp_board:
        copy_left_board.append(row)

    for j in range(N):
        for i in range(N):
            if copy_left_board[i][j] != 0:



    queue.append((copy_left_board, count + 1))

    # Right
    # copy right board
    copy_right_board = []
    for row in temp_board:
        copy_right_board.append(row)
    for i in range(N):
        for j in range(N):
            if copy_right_board[i][j] != 0:


    queue.append((copy_right_board, count + 1))

print(answer)





