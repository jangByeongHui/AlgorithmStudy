import sys

stairOfNum=int(sys.stdin.readline())
stairOfPoint=[]

dp = [0 for _ in range(stairOfNum)]

# 계단별 점수 확인
for _ in range(stairOfNum):
    stairOfPoint.append(int(sys.stdin.readline()))
try:
    dp[0]=stairOfPoint[0]
    dp[1]=stairOfPoint[0]+stairOfPoint[1]
    dp[2]=max(dp[0]+stairOfPoint[2],stairOfPoint[1]+stairOfPoint[2])

    for i in range(3,stairOfNum):
        dp[i]=max(dp[i-2]+stairOfPoint[i],dp[i-3]+stairOfPoint[i-1]+stairOfPoint[i])
except:
    if stairOfNum==3:
        dp[0] = stairOfPoint[0]
        dp[1] = stairOfPoint[0] + stairOfPoint[1]
        dp[2] = max(dp[0] + stairOfPoint[2], stairOfPoint[1] + stairOfPoint[2])
    if stairOfNum==2:
        dp[0] = stairOfPoint[0]
        dp[1] = stairOfPoint[0] + stairOfPoint[1]
    if stairOfNum==1:
        dp[0] = stairOfPoint[0]

print(dp[stairOfNum-1])

