import sys

N , M = map(int,sys.stdin.readline().split())

user_distance = [[None for _ in range(N)] for _ in range(N)]

for i in range(N):
    user_distance[i][i]=0

for _ in range(M):
    src_user,des_user = map(int,sys.stdin.readline().split())
    user_distance[src_user-1][des_user-1]=1
    user_distance[des_user - 1][src_user - 1] = 1

for user in user_distance:
    for num,other_user in enumerate(user):
        if other_user is None:




print(user_distance)