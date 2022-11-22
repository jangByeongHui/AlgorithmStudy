N = int(input())
a = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if a[i] < a[i-1]:
        x, y = i-1, i
        for j in range(N-1, 0, -1):
            if a[j] < a[x]:
                a[j], a[x] = a[x], a[j]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(*a)
                exit(0)
print(-1)

# https://velog.io/@y7y1h13/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-10973%EB%B2%88-%EC%9D%B4%EC%A0%84-%EC%88%9C%EC%97%B4python