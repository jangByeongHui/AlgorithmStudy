import sys

input = sys.stdin.readline

N = int(input().rstrip())

T,P = [],[]
dp = [0 for _ in range(N+1)]

for _ in range(N):
    t,p = map(int,input().rstrip().split())

    T.append(t)
    P.append(p)

for i in range(N-1,-1,-1):
    if T[i]+i <= N:
        dp[i] = max(dp[i+1],P[i]+dp[i+T[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])