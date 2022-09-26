import sys

input = sys.stdin.readline

N = int(input().rstrip())

room = []

answer = 0

for _ in range(N):
    room.append(list(map(int,input().rstrip().split())))


queue = [(0,0,0,1)]


while queue:
    px1, py1, px2, py2 = queue.pop()
    if px2 == N-1 and py2 == N-1:
        answer += 1
        continue

    # 오른쪽 이동
    if (px1 == px2 or (px1 != px2 and py1 != py2)) and 0 <= py2+1 < N and room[px2][py2+1] == 0:
        queue.append((px2,py2,px2,py2+1))

    # 아래로 이동
    if (py1 == py2 or (px1 != px2 and py1 != py2)) and 0 <= px2+1 < N and room[px2+1][py2] == 0:
        queue.append((px2,py2,px2+1,py2))

    # 대각선 이동
    if 0 <= px2 + 1 < N and 0 <= py2 + 1 < N and room[px2][py2+1] == 0 and room[px2+1][py2] == 0 and room[px2+1][py2+1] == 0:
        queue.append((px2,py2,px2+1,py2+1))

print(answer)