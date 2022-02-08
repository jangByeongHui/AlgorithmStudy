import sys
import math

num=int(sys.stdin.readline())

dp=[4 for _ in range(num+1)]
dp[0]=0
dp[1]=1

for i in range(2,num+1):
    for j in range(int(math.sqrt(i)+1)):
        dp[i]=min(dp[i],dp[i-j**2])
    dp[i]+=1


print(dp[num])



