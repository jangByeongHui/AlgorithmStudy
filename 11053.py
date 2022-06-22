import sys

input = sys.stdin.readline

N = int(input()) # 수열 크기

arr = list(map(int, input().split())) # 수열 정보 얻기
dp = [1]*N


# arr 탐색
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1) # dp 갱신

print(max(*dp))