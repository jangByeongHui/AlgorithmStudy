import sys

input = sys.stdin.readline

# 데이터 입력 받기
N, L = map(int, input().rstrip().split())

space = []

for _ in range(N):
    space.append(list(map(int,input().rstrip().split())))

answer = 0

# 주어진 경로가 지나갈 수 있는 길인지 판단하는 함수
def check_path(path,n,l):

    # 해당 경로의 높이가 모두 같은 경우
    before = path[0]
    for i in range(1,n):
        if before != path[i]:
            break
    else:
        return True

    # 경사로를 설치하여 갈 수 있는 길인 경우
    before = path[0]
    visited = [False for _ in range(n)]
    for i in range(1,n):
        if abs(before-path[i]) > 1: # 이전과 높이 차가 1 초과이면 경사로 설치 불가
            break

        if before < path[i]: # 낮은 곳에서 높은 곳으로 경사로 설치
            if i-l < 0:
                break
            for index in range(i-l,i):
                if before != path[index] or visited[index]:
                    return False
                visited[index] = True

        elif before > path[i]: # 높은 곳에서 낮은 곳으로 경사로 설치
            if i+l > n:
                break
            for index in range(i,i+l):
                if path[i] != path[index] or visited[index]:
                    return False
                visited[index] = True

        before = path[i] # 이전 값 기록

    else:
        return True

    # 어떠한 경우도 만족하지 않는다면 False
    return False

# 각 행에 대해서 계산
for i in range(N):
    test_path = space[i][:]
    if check_path(test_path,N,L):
        answer += 1

# 각 열에 대해서 계산
for i in range(N):
    test_path = []
    for j in range(N):
        test_path.append(space[j][i])
    if check_path(test_path,N,L):
        answer += 1

print(answer)
