import sys
from collections import deque

input = sys.stdin.readline

# 데이터 입력 확인
N, K = map(int,input().rstrip().split())

conveyor_belt = list(map(int, input().rstrip().split()))
conveyor_belt_with_robot = deque()

for health in conveyor_belt:
    conveyor_belt_with_robot.append([health,False])


def check_finish_condition(conveyor, k):
    count = 0
    for health in conveyor:
        if health[0] <= 0:
            count += 1

    if count >= k:
        return True
    return False

answer = 0

while True:
    if check_finish_condition(conveyor_belt_with_robot,K):
        break
    answer += 1

    # 컨베이어 벨트 이동
    conveyor_belt_with_robot.appendleft(conveyor_belt_with_robot.pop())
    # 로봇 탈출 위치
    if conveyor_belt_with_robot[N - 1][1]:
        conveyor_belt_with_robot[N - 1][1] = False

    # 로봇 움직이기
    for i in range(N-2,-1,-1):
        if conveyor_belt_with_robot[i][1] and not conveyor_belt_with_robot[i+1][1] and conveyor_belt_with_robot[i+1][0] > 0:
            conveyor_belt_with_robot[i+1][0] -= 1
            conveyor_belt_with_robot[i][1] = False
            conveyor_belt_with_robot[i+1][1] = True

    # 로봇 탈출 위치
    if conveyor_belt_with_robot[N-1][1]:
        conveyor_belt_with_robot[N-1][1] = False

    # 처음 위치 로봇 놓기
    if conveyor_belt_with_robot[0][0] > 0 and not conveyor_belt_with_robot[0][1]:
        conveyor_belt_with_robot[0][0] -= 1
        conveyor_belt_with_robot[0][1] = True

print(answer)