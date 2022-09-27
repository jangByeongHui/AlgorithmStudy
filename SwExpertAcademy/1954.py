
directions = [(0,1),(1,0),(0,-1),(-1,0)]

T = int(input())

for t in range(T):

    N = int(input())

    board = [[0 for _ in range(N)] for _ in range(N)]
    nx, ny = 0, 0
    dir_index = 0

    for number in range(1,N**2+1):

        board[nx][ny] = number
        dx, dy = directions[dir_index]

        if not (0 <= nx + dx < N and 0 <= ny+dy < N and board[nx+dx][ny+dy] == 0):
            dir_index = (dir_index+1)%4
            dx, dy = directions[dir_index]

        nx += dx
        ny += dy
    print(f"#{t+1}")
    for row in board:
        for element in row:
            print(element,end=" ")
        print()
