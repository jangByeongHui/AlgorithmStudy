import sys

N , M = map(int,sys.stdin.readline().split())

user_distance = [[99999 for _ in range(N)] for _ in range(N)]
bfs=[]

for i in range(N):
    user_distance[i][i]=0

for _ in range(M):
    src_user,des_user = map(int,sys.stdin.readline().split())
    user_distance[src_user-1][des_user-1]=1
    user_distance[des_user - 1][src_user - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            user_distance[i][j]=min(user_distance[i][j],user_distance[i][k]+user_distance[k][j])

Min_dist=9999
Min_user=0
for num,user in enumerate(user_distance):
    result=sum(user)

    if Min_dist>result:
        Min_dist=result
        Min_user=num+1



print(Min_user)