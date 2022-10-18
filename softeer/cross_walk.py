from collections import deque

N = int(input())


cars = deque()
now_time = 1e10
for id in range(N):

    time, type = input().split()
    time = int(time)
    now_time = min(now_time,time)
    cars.append({"start_time":time,"type":type,"id":id,"cross":False})


result = []
right_car = {"A":"D","B":"A","C":"B","D":"C"}

while cars:

    car = cars.popleft()

    # 이미 지나간 차량
    if car["cross"]:
        continue

    if car["start_time"] > now_time: # 아직 교차로에 진입할 때가 아님
        continue

    # 차량 위치 파악
    for next_car in cars:
        if next_car["cross"] or next_car["start_time"] > now_time: # 지나간 차량과 교차로에 진입하지 않은 차량은 무시
            continue
        # 오른쪽에 차량이 있음 다음에 통과
        if next_car["type"] == right_car[car["type"]]:
            cars.append(car)
            break
    else: # 어떠한 문제가 없음으로 교차로 통행
        result.append((car["id"],now_time))

    now_time += 1 # 매번 시간 증가

print(result)