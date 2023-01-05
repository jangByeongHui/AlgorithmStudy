import sys

input = sys.stdin.readline

while True:

    N = input().rstrip()

    if not N:
        break

    N = int(N)

    prices = list(map(int,input().rstrip().split()))

    dp = [0 for _ in range(N)]
    dp[0] = prices[0]
    length = 1

    for price in prices[1:]:
        start = 0
        end = length - 1
        index = 0

        while start <= end:

            mid = (start+end) // 2

            if dp[mid] < price:
                start = mid + 1
                index = max(index,mid+1)

            else:
                end = mid - 1

        length = max(length, index+1)
        dp[index] = price

    print(length)