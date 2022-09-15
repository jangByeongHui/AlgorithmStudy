import sys

input = sys.stdin.readline

directions = [(0,1), (1,0), (0,-1),(-1,0)]

# 데이터 입력
R, C, T = map(int, input().rstrip().split())

room_dust = []

for _ in range(R):
    room_dust.append(list(map(int, input().rstrip().split())))

# 먼지 확산 함수
def dust_diffusion(r, c, matrix):
    divide_dust = [[0 for _ in range(c)] for _ in range(r)] # 먼지 확산으로 인한 증감 계산

    for row in range(r):
        for col in range(c):
            if matrix[row][col] > 0:
                move_point = []

                for dx, dy in directions:
                    Dx , Dy =  row + dx, col + dy

                    # 인접한 공간 찾기
                    if 0 <= Dx < r and 0 <= Dy < c:
                        if matrix[Dx][Dy] == -1:
                            continue
                        move_point.append((Dx,Dy))

                # 먼지 확산
                move_dust_amount = matrix[row][col]//5
                for mr, mc in move_point:
                    divide_dust[mr][mc] += move_dust_amount
                divide_dust[row][col] -= move_dust_amount*len(move_point)

    # 먼지 증감 적용
    for row in range(r):
        for col in range(c):
            matrix[row][col] += divide_dust[row][col]

def activation_air_purifier(r,c,matrix):

    top_air_purifier = (0, 0)
    bottom_air_purifier = (0, 0)

    # 공기 청정기 위 부분 찾기
    for row in range(r):
        if matrix[row][0] == -1:
            top_air_purifier = (row,0)
            break

    # 공기 청정기 아래 부분 찾기
    for row in range(r):
        if row != top_air_purifier[0] and matrix[row][0] == -1:
            bottom_air_purifier = (row, 0)
            break

    expected_move_dust = [[0 for _ in range(c)] for _ in range(r)]

    # 공기 청소기 윗 부분 순환
    startX, startY = top_air_purifier
    startY += 1

    while (startX, startY) != top_air_purifier:
        next_x = startX
        next_y = startY

        # 반 시계 방향으로 이동
        if startX == top_air_purifier[0] and 0 <= startY + 1 < c:
            next_y += 1
        elif 0 < startX <= top_air_purifier[0] and startY == c-1:
            next_x -= 1
        elif startX == 0 and 0 < startY < c:
            next_y -= 1
        else:
            next_x += 1
        expected_move_dust[next_x][next_y] = matrix[startX][startY]
        matrix[startX][startY] = 0
        startX, startY = next_x, next_y

    # 공기 청소기 아래 부분 순환
    startX, startY = bottom_air_purifier
    startY += 1

    while (startX, startY) != bottom_air_purifier:
        next_x = startX
        next_y = startY

        # 시계 방향으로 이동
        if startX == bottom_air_purifier[0] and 0 <= startY < c-1:
            next_y += 1
        elif bottom_air_purifier[0] <= startX < r-1 and startY == c - 1:
            next_x += 1
        elif startX == r-1 and 0 < startY < c:
            next_y -= 1
        else:
            next_x -= 1
        expected_move_dust[next_x][next_y] = matrix[startX][startY]
        matrix[startX][startY] = 0
        startX, startY = next_x, next_y

    for row in range(r):
        for col in range(c):
            if expected_move_dust[row][col] != 0 and matrix[row][col] != -1:
                matrix[row][col] = expected_move_dust[row][col]

def print_board(matrix):
    print("################################")
    for row in matrix:
        print(row)
    print("################################")

def calculate_result(r,c,matrix):
    result = 0

    for row in range(r):
        for col in range(c):
            if matrix[row][col] == -1:
                continue
            result += matrix[row][col]
    return result


for t in range(T):
    dust_diffusion(R,C,room_dust)
    #print_board(room_dust)
    activation_air_purifier(R, C, room_dust)
    #print_board(room_dust)

print(calculate_result(R,C,room_dust))