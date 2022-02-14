import sys

N,M =map(int,sys.stdin.readline().split())

num= list(map(int,sys.stdin.readline().split()))


dp=[[0 for _ in range(len(num))] for _ in range(len(num))]

for i in range(N):
    for j in range(i,N):
        dp[i][j]=num[j]+dp[i][j-1]

for _ in range(M):
    first, last = map(int,sys.stdin.readline().split())
    print(dp[first-1][last-1])