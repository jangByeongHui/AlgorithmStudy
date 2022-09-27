
for t in range(10):
    N = int(input())

    buildings = list(map(int,input().split()))

    answer = 0

    for i in range(N):
        left_1 = i - 2
        left_2 = i - 1

        right_1 = i + 2
        right_2 = i + 1

        if 0 <= left_1 and right_1 < N:

            left_min = min(buildings[i]-buildings[left_1],buildings[i]-buildings[left_2])
            right_min = min(buildings[i]-buildings[right_1],buildings[i]-buildings[right_2])

            if left_min > 0 and right_min > 0:
                answer += min(left_min,right_min)

    print(f"#{t+1} {answer}")