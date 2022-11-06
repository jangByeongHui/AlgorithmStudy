T = int(input())

for i in range(T) :

    N = int(input())

    dp = [0]*(N+1)

    if N == 1 :
        print(1)

    elif N == 2 :
        print(2)

    elif N == 3 :
        print(4)

    else :
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for j in range(4,N+1) :
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

        print(dp[N])

# 참고 : https://animoto1.tistory.com/entry/%EB%B0%B1%EC%A4%80-9095-123-%EB%8D%94%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python