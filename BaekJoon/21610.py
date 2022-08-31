import sys

#initialze
board = []
directions = [(0,-1), # 좌
              (-1,-1), # 좌상
              (-1,0), # 상
              (-1,1), # 우상
              (0,1), # 우
              (1,1), # 우하
              (1,0), # 하
              (1,-1)] # 좌하
diagonal_directions = [(1,1),(-1,1),(1,-1),(-1,-1)]
def print_matrix(index,name,mat):
    print(f"############# {index}_{name}#################")
    for row in mat:
        print(row)
    print("#####################################\n")

# init input data
N, M = map(int,input().rstrip().split())
cloud_board = [[0 for i in range(N)] for j in range(N)]
cloud_board[N-1][0] = 1
cloud_board[N-1][1] = 1
cloud_board[N-2][0] = 1
cloud_board[N-2][1] = 1

for _ in range(N):
    board.append(list(map(int,input().rstrip().split())))

for index in range(M):
    d, s = map(int,input().rstrip().split())
    dx, dy = directions[d-1]
    dx = s*dx
    dy = s*dy

    cloud_move_pos = []
    debug_move_pos = []
    print_matrix(index + 1, "before move cloud", cloud_board)
    # move cloud
    for i in range(N):
        for j in range(N):
            if cloud_board[i][j] > 0:
                cloud_board[i][j] = 0
                convert_x, convert_y = i + dx, j + dy

                if convert_x >= N:
                    convert_x = (i + dx) % N

                if convert_x < 0:
                    convert_x = -((i + dx) % N)
                    if convert_x < 0:
                        convert_x = N + convert_x

                if convert_y >= N:
                    convert_y = (j+dy) % N

                if convert_y < 0:
                    convert_y = -((j + dy) % N)
                    if convert_y < 0:
                        convert_y = N + convert_y
                cloud_move_pos.append((convert_x, convert_y))
                debug_move_pos.append((i,j,convert_x,convert_y))

    for x,y,cx,cy in debug_move_pos:
       print(f"x: {x} y: {y} - > x: {cx} y: {cy}")

    # fill the water by cloud
    for mx, my in cloud_move_pos:
        count = 0
        try:
            cloud_board[mx][my] = -1  # remove cloud
            board[mx][my] += 1
        except:
            print("error index",mx,my)
        for diagonal_dx, diagonal_dy in diagonal_directions:
            diagonal_x, diagonal_y = mx + diagonal_dx, my + diagonal_dy
            if 0 <= diagonal_x < N and 0 <= diagonal_y < N and board[diagonal_x][diagonal_y] > 0:
                count += 1
        board[mx][my] += count
    print_matrix(index + 1, "after move cloud", cloud_board)
    # Debug print
    print_matrix(index + 1, "board", board)

    # make cloud by water bottle
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1 and cloud_board[i][j] != -1:
                board[i][j] -= 2
                cloud_board[i][j] = 1

    #clear remove cloude marking
    for mx, my in cloud_move_pos:
        cloud_board[mx][my] = 0


result = 0

for row in board:
    result += sum(row)

print(result)








