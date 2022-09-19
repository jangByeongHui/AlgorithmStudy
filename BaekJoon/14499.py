import sys

input = sys.stdin.readline

# 값 초기화
dice = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

directions = [(0,0),(0,1),(0,-1),(-1,0),(1,0)]

# 데이터 입력
N, M, X, Y, K = map(int,input().rstrip().split())

board = []

for _ in range(N):
    board.append(list(map(int,input().rstrip().split())))

orders = list(map(int,input().rstrip().split()))


# 주사위 놓기
def copy_dice_or_board(r,c):

    if board[r][c] == 0:
        board[r][c] = dice[1][1]

    else:
        dice[1][1] = board[r][c]
        board[r][c] = 0


# 주사위 굴리기
def roll_dice(index):
    if index == 1:
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1],dice[1][2], dice[3][1], dice[1][0]
    elif index == 2:
        dice[1][1], dice[1][0], dice[1][2], dice[3][1] = dice[1][0], dice[3][1], dice[1][1], dice[1][2]
    elif index == 3:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif index == 4:
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

copy_dice_or_board(X,Y)

for order in orders:

    dx, dy = directions[order]

    if 0 <= X+dx < N and 0 <= Y+dy < M:
        X, Y = X+dx, Y+dy
        roll_dice(order)
        copy_dice_or_board(X,Y)
        print(dice[3][1])


