from collections import deque, defaultdict

N = int(input())


cars = deque()
now_time = 1e10
for id in range(N):

    time, type = input().split()
    time = int(time)
    now_time = min(now_time,time)
    cars.append({"start_time":time,"end_time":-1,"type":type,"id":id,"cross":False})


result = []
right_car = {"A":"D","B":"A","C":"B","D":"C"}

while True:

    # 모든 차량이 교차로를 통과하였다면 종료
    for car in cars:
        if not car["cross"]:
            break
    else:
        break

    candidate_cars = deque()

    # 지나갈 수 있는 차량 선별
    pass_car = defaultdict(bool)
    for car in cars:
        if car["start_time"] > now_time or car["cross"]: # 시간이 되지 않았거나 지나간 차량은 제외
            continue
        if pass_car[car["type"]]:
            continue
        pass_car[car["type"]] = True # 한 교차로에서 한번만 지나 다닐 수 있음으로 이미 선택한 교차로는 pass
        candidate_cars.append(car)

    # 교착 상태에 도달하는지 판단
    A, B, C, D = False, False, False, False

    for candidate in candidate_cars:
        if candidate["type"] == "A":
            A = True
        elif candidate["type"] == "B":
            B = True
        elif candidate["type"] == "C":
            C = True
        else:
            D = True

    if A and B and C and D: # 교착 상태에 도달하였음으로 종료
        break

    for car_index,car in enumerate(candidate_cars): # 최대 비교를 4*4만 하게 됨

        for next_car_index,next_car in enumerate(candidate_cars):
            if car_index == next_car_index: # 자기 자신 비교는 skip
                continue
            if right_car[car["type"]] == next_car["type"]: # 오른쪽에 차량이 위치하고 있으면 지나 갈 수 없음
                break
        else: # 지나갈 수 있음
            car["end_time"] = now_time
            car["cross"] = True

    now_time += 1

for car in cars:
    print(car["end_time"])