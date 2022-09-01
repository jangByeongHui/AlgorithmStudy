import sys

input = sys.stdin.readline
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
all_even_odd_dir = [0,2,4,6]
all_not_even_odd_dir = [1,3,5,7]

# custom function
def move_fire_ball(x,y,s,d,N):
    dx, dy = directions[d]

    new_x = x + s*dx
    new_y = y + s*dy

    if new_x >= N:
        new_x = new_x % N

    if new_y >= N:
        new_y = new_y % N

    if new_x < 0:
        new_x = new_x %(N)
        if new_x < 0:
            new_x = N - new_x

    if new_y < 0:
        new_y = new_y %(N)
        if new_y < 0:
            new_y = N - new_y

    return new_x,new_y

# initialize data
N, M, K = map(int, input().rstrip().split())

board = [[[] for _ in range(N)]for _ in range(N)]
fire_balls = [[[] for _ in range(N)]for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input().rstrip().split())

    fire_balls[r-1][c-1].append((m,s,d)) # 좌표에 따른 파이어볼 추가


for index in range(K):
    new_fire_balls = [[[] for _ in range(N)]for _ in range(N)]

    # move fire ball
    for i in range(N):
        for j in range(N):
            while fire_balls[i][j]:
                mi,si,di = fire_balls[i][j].pop()
                new_ri, new_ci = move_fire_ball(i,j,si,di,N) # 이동 방향에 맞추어 새로운 좌표로 이동
                new_fire_balls[new_ri][new_ci].append((mi,si,di)) # 해당 좌표에 파이어볼 추가

    # check divide fire ball
    for i in range(N):
        for j in range(N):
            if len(new_fire_balls[i][j]) > 1:
                fire_ball_count = len(new_fire_balls[i][j])
                M = 0
                S = 0
                D = []

                while new_fire_balls[i][j]:

                    mi, si, di = new_fire_balls[i][j].pop()
                    M += mi
                    S += si
                    D.append(di)

                new_M = M//5
                new_S = S//fire_ball_count

                if new_M > 0: #check divide condition
                    all_dir_odd = True
                    all_dir_even = True


                    for d in D:
                        if d % 2 == 0:
                            all_dir_odd = False
                            break

                    for d in D:
                        if d % 2 != 0:
                            all_dir_even = False

                    if all_dir_odd or all_dir_even:
                        for d in all_even_odd_dir:
                            new_fire_balls[i][j].append((new_M,new_S,d))
                    else:
                        for d in all_not_even_odd_dir:
                            new_fire_balls[i][j].append((new_M,new_S,d))
    fire_balls = new_fire_balls

# Sum all fire ball Material
result = 0
for i in range(N):
    for j in range(N):
        while fire_balls[i][j]:
            mi, si, di = fire_balls[i][j].pop()
            result += mi

print(result)