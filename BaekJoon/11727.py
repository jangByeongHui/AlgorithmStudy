import sys

n = int(sys.stdin.readline())

dp = [2*i+1 for i in range(n+1)]

for i in range(2,n):
    dp[i] = dp[i-1]+2*dp[i-2]

print(dp[n-1]%10007)