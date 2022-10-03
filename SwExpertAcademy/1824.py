from collections import deque
from collections import defaultdict
T = int(input())

def move_left(cur_row,cur_col,max_row_len,max_col_len):

    if 0 <= cur_col - 1:
        return (cur_row,cur_col-1)
    else:
        return (cur_row,max_col_len-1)

def move_right(cur_row,cur_col,max_row_len,max_col_len):

    if cur_col + 1 < max_col_len:
        return (cur_row,cur_col+1)
    else:
        return (cur_row,0)

def move_up(cur_row,cur_col,max_row_len,max_col_len):

    if  0<= cur_row - 1:
        return (cur_row-1,cur_col)
    else:
        return (max_row_len-1,cur_col)


def move_down(cur_row, cur_col, max_row_len, max_col_len):
    if cur_row + 1 < max_row_len:
        return (cur_row + 1 , cur_col)
    else:
        return (0, cur_col)


for index in range(1,T+1):
    row, col = map(int,input().split())

    commands = []
    visited = defaultdict(bool)
    state = "x:{}y:{}memory:{}direction:{}"
    for _ in range(row):
        commands.append(input())

    answer = "NO"
    queue = deque([(0,0,0,"right")])

    while queue:

        x, y, memory, direction = queue.popleft()

        if visited[state.format(x,y,memory,direction)]:
            continue
        visited[state.format(x,y,memory,direction)] = True

        if commands[x][y] == "<":
            direction = "left"
        elif commands[x][y] == ">":
            direction = "right"
        elif commands[x][y] == "^":
            direction = "up"
        elif commands[x][y] == "v":
            direction = "down"
        elif commands[x][y] == "_":
            if memory == 0:
                direction = "right"
            else:
                direction = "left"
        elif commands[x][y] == "|":
            if memory == 0:
                direction = "down"
            else:
                direction = "up"

        elif commands[x][y] == "?":
            nx, ny = move_left(x,y,row,col)
            queue.append((nx,ny,memory,"left"))

            nx, ny = move_right(x, y, row, col)
            queue.append((nx, ny,memory, "right"))

            nx, ny = move_up(x, y, row, col)
            queue.append((nx, ny,memory, "up"))

            nx, ny = move_down(x, y, row, col)
            queue.append((nx, ny,memory, "down"))
            continue

        elif commands[x][y] == ".":
            pass

        elif commands[x][y] == "@":
            answer = "YES"
            break

        elif commands[x][y].isdigit() and 0 <= int(commands[x][y]) <= 9:
            memory = int(commands[x][y])

        elif commands[x][y] == "+":
            memory = (memory+1)%16

        elif commands[x][y] == "-":
            if memory == 0:
                memory = 15
            else:
                memory -= 1

        if direction == "left":
            nx, ny = move_left(x,y,row,col)
            if not visited[state.format(nx,ny,memory,"left")]:
                queue.append((nx,ny,memory,"left"))
        elif direction == "right":
            nx, ny = move_right(x, y, row, col)
            if not visited[state.format(nx,ny,memory,"right")]:
                queue.append((nx, ny, memory, "right"))

        elif direction == "up":
            nx, ny = move_up(x, y, row, col)
            if not visited[state.format(nx,ny,memory,"up")]:
                queue.append((nx, ny, memory, "up"))

        elif direction == "down":
            nx, ny = move_down(x, y, row, col)
            if not visited[state.format(nx,ny,memory,"down")]:
                queue.append((nx, ny, memory, "down"))

    print(f"#{index} {answer}")