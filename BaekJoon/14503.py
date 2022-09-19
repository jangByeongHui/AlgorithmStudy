import sys

input = sys.stdin.readline

# 초기 데이터 설정
# 북쪽 - > 서쪽 ,동쪽 -> 북쪽, 남쪽 -> 동쪽, 서쪽 -> 남쪽
left_move = [(0,-1),(-1,0),(0,1),(1,0)]
# 북쪽 -> 남쪽, 동쪽 -> 서쪽, 남쪽 -> 북쪽, 서쪽 -> 동쪽
back_move = [(1,0),(0,-1),(-1,0),(0,1)]

# 함수 정의
def find_next_dir(direction):
    if direction == 0:
        return 3
    elif direction == 1:
        return 0
    elif direction == 2:
        return 1
    elif direction == 3:
        return 2


# 데이터 입력
N, M = map(int, input().rstrip().split())


robot_init_r, robot_init_c, robot_init_dir = map(int, input().rstrip().split())


space = []

for _ in range(N):
    space.append(list(map(int,input().rstrip().split())))

visited = [[False for _ in range(M)] for _ in range(N)]

robot = {'r':robot_init_r,'c':robot_init_c,'dir':robot_init_dir}
index = 1
while True:

    # 로봇에 왼쪽 방향을 확인
    visited[robot['r']][robot['c']] = True
    dr, dc = left_move[robot['dir']]
    left_r, left_c = robot['r']+dr, robot['c']+dc
    if 0 <= left_r < N and 0 <= left_c < M and space[left_r][left_c] == 0 and not visited[left_r][left_c]:
        robot['r'] = left_r
        robot['c'] = left_c
        robot['dir'] = find_next_dir(robot['dir'])

    else:
        # 네 방향 중 왼쪽으로 회전 해보면서 청소할 수 있는 곳 확인
        temp_dir = robot['dir']

        for _ in range(3):
            temp_dir = find_next_dir(temp_dir)
            tr, tc = left_move[temp_dir]
            t_left_r, t_left_c = robot['r']+tr,robot['c']+tc
            if 0 <= t_left_r < N and 0 <= t_left_c < M and space[t_left_r][t_left_c] == 0 and not visited[t_left_r][t_left_c]:
                robot['dir'] = temp_dir
                break

        else: # 네 방향 모두 청소가 되어있거나 벽인 경우
            br, bc = back_move[robot['dir']]
            back_r, back_c = robot['r']+br, robot['c']+bc

            if 0 <= back_r < N and 0 <= back_c < M and space[back_r][back_c] == 0: # 후진이 가능한 경우
                robot['r'] = back_r
                robot['c'] = back_c
            else: # 후진 또한 불가능하면 로봇 종료
                break

answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]:
            answer += 1
print(answer)
