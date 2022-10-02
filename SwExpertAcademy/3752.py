T = int(input())

def solution(index):

    N = int(input())
    scores = list(map(int,input().split()))

    scores_sum = sum(scores)
    dp = [False] * (scores_sum+1)

    dp[0] = True

    for num in scores:
        for idx in range(scores_sum,-1,-1):
            if dp[idx] == True:
                dp[idx+num] = True

    print(f"#{index+1} {dp.count(True)}")

for index in range(T):
    solution(index)