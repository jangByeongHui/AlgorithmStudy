import sys
from collections import Counter

input = sys.stdin.readline

# 데이터 입력
r, c, k = map(int, input().rstrip().split())

board = []

for _ in range(3):
    board.append(list(map(int,input().rstrip().split())))

def cal_r():
    global board
    temp_board = []
    max_row_len = -sys.maxsize

    for row in board:

        temp_tuple = []
        # 빈도수 추출
        for (key, value) in Counter(row).items():
            if key == 0:
                continue
            temp_tuple.append((key,value))

        # 제시 기준으로 정렬
        temp_tuple.sort(key= lambda x:(x[1],x[0]))

        # 변형된 행 생성
        temp_row = []
        for key,value in temp_tuple:
            temp_row.append(key)
            temp_row.append(value)

        max_row_len = max(max_row_len,len(temp_row)) # 짧은 행에 0을 추가하기 위함
        temp_board.append(temp_row)  # 계산된 행

    for row in temp_board:
        for _ in range(max_row_len-len(row)):
            row.append(0)

    # 새로 변경된 행렬로 변경
    board = temp_board

def cal_c():
    global board
    row_len = len(board)
    col_len = len(board[0])

    temp_board = []

    # 행렬 변환
    for j in range(col_len):
        temp_row = []
        for i in range(row_len):
            temp_row.append(board[i][j])
        temp_board.append(temp_row)

    board = temp_board

    cal_r() # 같은 연산

    # 행렬변환
    row_len = len(board)
    col_len = len(board[0])
    temp_board = []
    for j in range(col_len):
        temp_row = []
        for i in range(row_len):
            temp_row.append(board[i][j])
        temp_board.append(temp_row)

    board = temp_board

for answer in range(101):

    if board[r-1][c-1] == k:
        print(answer)
        break

    if len(board) >= len(board[0]):
        cal_r()
    else:
        cal_c()

else:
    print(-1)
