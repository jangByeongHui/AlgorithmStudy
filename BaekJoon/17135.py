import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

N, M, D = map(int,input().rstrip().split())

castle = []
enemies = []

for i in range(N):
    row = list(map(int,input().rstrip().split()))
    castle.append(row)
    for j, element in enumerate(row):
        if element == 1:
            enemies.append({"x":i,"y":j,"alive":True,"ingame":True})

answer = 0

def count_kill(enemies):
    count = 0
    for enemy in enemies:
        if not enemy["alive"]:
            count += 1
    return count

for archers_y in combinations(range(M),3):
    archers = []
    temp_enemies = deepcopy(enemies)
    # 궁수 배치
    for archer_y in archers_y:
        archers.append((N,archer_y))

    # 적이 사라질 때까지 게임 진행
    while True:
        # 궁수 공격

        for archer_x, archer_y in archers:
            kill_candidate = []
            for index, enemy in enumerate(temp_enemies):

                if not enemy["ingame"]:
                    continue

                temp_distance = abs(archer_x-enemy['x']) + abs(archer_y-enemy['y'])
                if temp_distance <= D:
                    kill_candidate.append((index,enemy['y'],temp_distance))

            if len(kill_candidate) > 0:
                kill_candidate.sort(key = lambda x:(x[2],x[1])) # 가장 가깝고 가장 왼쪽에 있는 적

                temp_enemies[kill_candidate[0][0]]["alive"] = False # 적 제거

        # 궁수에 의해 죽은 적들은 게임에서 제외
        for index in range(len(temp_enemies)):
            if not temp_enemies[index]["alive"]:
                temp_enemies[index]["ingame"] = False

        # 적 이동
        for index,enemy in enumerate(temp_enemies):
            if not enemy["ingame"] or not enemy["alive"]:
                continue

            temp_enemies[index]["x"] += 1
            # 성에 도달한 적
            if temp_enemies[index]["x"] >= N:
                temp_enemies[index]["ingame"] = False

        # 종료 조건
        for enemy in temp_enemies:
            # 단 하나라도 게임에 있다면 게임 지속
            if enemy["ingame"]:
                break
        else:
            # 모든 적이 게임에 없음으로 게임 종료
            break

    answer = max(answer,count_kill(temp_enemies))
print(answer)