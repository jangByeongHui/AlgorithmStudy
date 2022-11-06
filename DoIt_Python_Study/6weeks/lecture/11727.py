N = int(input())

dp = [2*i+1 for i in range(N+1)]

for i in range(2,N):
    dp[i] = dp[i-1]+2*dp[i-2] # 참고 : https://jokerldg.github.io/algorithm/2021/07/26/2xn-tiling2.html
print(dp[N-1]%10007)