import sys

Inter = int(sys.stdin.readline())

for _ in range(Inter):
    num = int(sys.stdin.readline())

    dp=[0 for i in range(num+1)]
    try:
        dp[1]=1
        dp[2]=2
        dp[3]=4
    except:
        pass

    for i in range(4,num+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[num])