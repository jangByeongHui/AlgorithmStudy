from collections import deque

# 함수 정의
def gear_rotate(gear, clockwise):

    if clockwise == 1:
        gear.appendleft(gear.pop()) # 반시계 방향
    else:
        gear.append(gear.popleft()) # 시계 방향

def all_gears_rotate(gears,target_gear,target_clockwise):

    rotated = [False]*4
    queue = deque([(target_gear-1,target_clockwise)])
    rotate_candidation = []

    while queue:
        cur_gear, cur_clockwise = queue.popleft()

        rotate_candidation.append((cur_gear,cur_clockwise)) # 한번에 회전 시키기 위함
        rotated[cur_gear] = True

        if cur_gear == 0:
            if not rotated[1] and gears[0][2] != gears[1][6]:
                queue.append((1,cur_clockwise*-1))

        elif cur_gear == 1:
            if not rotated[0] and gears[1][6] != gears[0][2]:
                queue.append((0,cur_clockwise*-1))
            if not rotated[2] and gears[1][2] != gears[2][6]:
                queue.append((2,cur_clockwise*-1))

        elif cur_gear == 2:
            if not rotated[1] and gears[2][6] != gears[1][2]:
                queue.append((1,cur_clockwise*-1))
            if not rotated[3] and gears[2][2] != gears[3][6]:
                queue.append((3,cur_clockwise*-1))
        else:
            if not rotated[2] and gears[3][6] != gears[2][2]:
                queue.append((2,cur_clockwise*-1))

    # 모두 한번에 회전
    for target, wise in rotate_candidation:
        gear_rotate(gears[target],wise)

#데이터 입력
gears = deque()
for _ in range(4):
    str_gear = input()
    temp_gear = deque()

    for s in str_gear:
        temp_gear.append(int(s))

    gears.append(temp_gear)

# 톱니 바퀴 돌리기
K = int(input())

for _ in range(K):
    gear_number, clockwise = map(int,input().split())
    all_gears_rotate(gears,gear_number,clockwise)

# 결과
print(gears[0][0]+gears[1][0]*2+gears[2][0]*4+gears[3][0]*8)