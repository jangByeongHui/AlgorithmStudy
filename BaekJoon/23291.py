import sys
from collections import deque

input = sys.stdin.readline

#input data
N, K = map(int, input().rstrip().split())

fishes = list(map(int,input().rstrip().split()))
max_value = max(fishes)
min_value = min(fishes)
directions = [(1,0),(0,1)] # 위에서 아래로 비교하니 좌, 상은 비교 불필요

answer = 0

while max_value - min_value > K:

    # step1. increase min fishes
    for i in range(N):
        if fishes[i] == min_value:
            fishes[i] += 1

    # step2. stacking fish ball
    stacking_fish_ball = [[fishes[0]], fishes[1:]]

    row_len = len(stacking_fish_ball)
    col_len = len(stacking_fish_ball[0])

    while  len(stacking_fish_ball[-1][col_len:]) >= row_len:
        temp_stacking_fish_ball = []

        for col in range(col_len): # 2
            new_row = deque([])
            for row in range(row_len): # 3
                new_row.appendleft(stacking_fish_ball[row][col])
            temp_stacking_fish_ball.append(new_row)
        temp_stacking_fish_ball.append(stacking_fish_ball[-1][col_len:]) # 남은 요소 모두 추가

        row_len = len(temp_stacking_fish_ball)
        col_len = len(temp_stacking_fish_ball[0])
        stacking_fish_ball = temp_stacking_fish_ball

    # step3. adjust Fish count
    adjust_fish_value = [[0 for _ in range(len(row))] for row in stacking_fish_ball]

    min_col_len = len(stacking_fish_ball[0])
    max_col_len = len(stacking_fish_ball[-1])

    # step3-1. calculate fish move
    for i in range(row_len):
        for j in range(max_col_len):
            for dx,dy in directions:
                if 0 <= i+dx < row_len and 0 <= j < min_col_len and 0 <= j+dy < min_col_len:
                    value = abs(stacking_fish_ball[i][j]-stacking_fish_ball[i+dx][j+dy])//5

                    if stacking_fish_ball[i][j] < stacking_fish_ball[i+dx][j+dy]:
                        adjust_fish_value[i][j] += value
                        adjust_fish_value[i+dx][j+dy] -= value
                    else:
                        adjust_fish_value[i][j] -= value
                        adjust_fish_value[i + dx][j + dy] += value
                elif dx == 0 and i == row_len-1 and 0 <= j+dy < max_col_len:
                    value = abs(stacking_fish_ball[i][j] - stacking_fish_ball[i][j+dy])//5

                    if stacking_fish_ball[i][j] < stacking_fish_ball[i][j+dy]:
                        adjust_fish_value[i][j] += value
                        adjust_fish_value[i][j+dy] -= value
                    else:
                        adjust_fish_value[i][j] -= value
                        adjust_fish_value[i][j+dy] += value


    # step3-2. apply fish move
    for i in range(row_len):
        for j in range(len(stacking_fish_ball[i])):
            stacking_fish_ball[i][j] += adjust_fish_value[i][j]

    # step4. Flatten fish ball - 그림8
    flatten_row_len = len(stacking_fish_ball)
    flatten_col_len = len(stacking_fish_ball[0])
    flatten_fish_ball = []

    for j in range(flatten_col_len):
        flatten_row = deque()
        for i in range(flatten_row_len):
            flatten_row.appendleft(stacking_fish_ball[i][j])

        for element in flatten_row:
            flatten_fish_ball.append(element)
    for rest_elem in stacking_fish_ball[flatten_row_len-1][flatten_col_len:]:
        flatten_fish_ball.append(rest_elem)

    # step5. divide half flatten fish ball
    flatten_fish_ball_len = len(flatten_fish_ball)
    divide_fish_ball_first = [flatten_fish_ball[:flatten_fish_ball_len//2][::-1],flatten_fish_ball[flatten_fish_ball_len//2:]]

    divide_fish_ball_second = deque()
    divide_fish_ball_first_row_len = len(divide_fish_ball_first)
    divide_fish_ball_first_col_len = len(divide_fish_ball_first[0])

    for i in range(divide_fish_ball_first_row_len):
        new_row = deque()
        for j in range(divide_fish_ball_first_col_len//2):
            new_row.appendleft(divide_fish_ball_first[i][j])
        divide_fish_ball_second.appendleft(new_row)

    for i in range(divide_fish_ball_first_row_len):
        new_row = []
        for j in range(divide_fish_ball_first_col_len//2,divide_fish_ball_first_col_len):
            new_row.append(divide_fish_ball_first[i][j])
        divide_fish_ball_second.append(new_row)

    # step6. adjust Fish count
    adjust_row_len = len(divide_fish_ball_second)
    adjust_col_len = len(divide_fish_ball_second[0])
    adjust_fish_value = [[0 for _ in range(adjust_col_len)] for row in range(adjust_row_len)]


    for i in range(adjust_row_len):
        for j in range(adjust_col_len):
            for dx, dy in directions:
                if 0 <= i+dx < adjust_row_len and 0 <= j+dy < adjust_col_len:
                    value = abs(divide_fish_ball_second[i][j]-divide_fish_ball_second[i+dx][j+dy])//5
                    if divide_fish_ball_second[i][j] < divide_fish_ball_second[i+dx][j+dy]:
                        adjust_fish_value[i][j] += value
                        adjust_fish_value[i+dx][j+dy] -= value

                    else:
                        adjust_fish_value[i][j] -= value
                        adjust_fish_value[i + dx][j + dy] += value
    for i in range(adjust_row_len):
        for j in range(adjust_col_len):
            divide_fish_ball_second[i][j] += adjust_fish_value[i][j]

    # step7. Final Flatten
    final_fishes = []
    for j in range(adjust_col_len):
        for i in range(adjust_row_len-1,-1,-1):
            final_fishes.append(divide_fish_ball_second[i][j])

    fishes = final_fishes
    answer += 1
    max_value = max(fishes)
    min_value = min(fishes)

print(answer)