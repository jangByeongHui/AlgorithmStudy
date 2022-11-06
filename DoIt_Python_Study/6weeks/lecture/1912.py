N = int(input())
elements = list(map(int, input().split()))

for i in range(1, N):
    elements[i] = max(elements[i], elements[i] + elements[i - 1])

print(max(elements))

# 참고 : https://data-marketing-bk.tistory.com/52