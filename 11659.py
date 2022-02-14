import sys

N,M =map(int,sys.stdin.readline().split())

num= list(map(int,sys.stdin.readline().split()))
dp = [0 for _ in range(len(num)+1)]

for i in range(1,len(num)+1):
    dp[i]=dp[i-1]+num[i-1]

for _ in range(M):
    first, last = map(int,sys.stdin.readline().split())
    print(dp[last]-dp[first-1])