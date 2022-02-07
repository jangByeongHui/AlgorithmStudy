import sys
import math

def cal(num):
    count = 0
    while num >= 1:
        count += 1
        num -= math.pow(int(math.sqrt(num)), 2)
    return count

num=int(sys.stdin.readline())

dp=[0 for _ in range(num+1)]
dp[1]=1

for i in range(2,num+1):
    dp[i]=min(dp[i-1]+1,cal(i))

print(dp[num])



