N = int(input())

a = list(map(int, input().split()))

dp = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
# 참고 : https://zidarn87.tistory.com/285