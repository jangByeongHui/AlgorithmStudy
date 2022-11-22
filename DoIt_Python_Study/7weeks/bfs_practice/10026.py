import sys
from collections import deque
scan = sys.stdin.readline

N = int(scan())
img_ori = []
img_abnormal = []

visited = [[False for _ in range(N)] for _ in range(N)]
visited_abnormal = [[False for _ in range(N)] for _ in range(N)]

# 이미지 값 가져오기
for _ in range(N):
    row = scan()
    temp_abnormal = []
    temp = []
    for i in range(N):
        if row[i] == 'R':
            temp_abnormal.append('G')
        else:
            temp_abnormal.append(row[i])
        temp.append(row[i])
    img_ori.append(temp)
    img_abnormal.append(temp_abnormal)

dx=[1,0,-1,0]
dy=[0,1,0,-1]

bfs = []
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j]==False:
            visited[i][j]=True
            check_color = img_ori[i][j]
            bfs.append((i,j))
            while bfs:
                x,y = bfs.pop()
                visited[x][y]=True
                for k in range(4):
                    if 0<=x+dx[k]<N and 0<=y+dy[k]<N:
                        if visited[x+dx[k]][y+dy[k]] == False and check_color == img_ori[x+dx[k]][y+dy[k]]:
                            bfs.append((x+dx[k],y+dy[k]))
            count += 1

bfs = []
ab_count = 0
for i in range(N):
    for j in range(N):
        if visited_abnormal[i][j]==False:
            visited_abnormal[i][j]=True
            check_color = img_abnormal[i][j]
            bfs.append((i,j))
            while bfs:
                x,y = bfs.pop()
                visited_abnormal[x][y]=True
                for k in range(4):
                    if 0<=x+dx[k]<N and 0<=y+dy[k]<N:
                        if visited_abnormal[x+dx[k]][y+dy[k]]==False and check_color == img_abnormal[x+dx[k]][y+dy[k]]:
                            bfs.append((x+dx[k],y+dy[k]))
            ab_count += 1

print(count,ab_count)