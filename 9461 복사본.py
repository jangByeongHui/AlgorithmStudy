import sys

n=int(sys.stdin.readline())

for _ in range(n):
    dp=[0,1,1,1,2]
    num=int(sys.stdin.readline())
    for i in range(5,num+1):
        dp.append(dp[i-5]+dp[i-1])
    print(dp[num])