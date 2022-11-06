N = int(input())


dp =[i for i in range(1,N+1)]

for i in range(2,N):

    dp[i] = dp[i-1]+dp[i-2]
    # 참고 : https://assb.tistory.com/entry/%EB%B0%B1%EC%A4%80-11726%EB%B2%88-2xn-%ED%83%80%EC%9D%BC%EB%A7%81

print(dp[N-1]%10007)