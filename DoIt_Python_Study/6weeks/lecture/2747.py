# 초기화
dp = [0]*(46)
dp[1] = 1
dp[2] = 1

N = int(input())

for i in range(3,N+1):
    dp[i] = dp[i-2]+dp[i-1]

print(dp[N])

