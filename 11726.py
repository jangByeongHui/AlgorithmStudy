import sys

n = int(sys.stdin.readline())


dp =[i for i in range(1,n+1)]

for i in range(2,n):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n-1])