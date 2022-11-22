# next_permutation 파이썬 구현

n = int(input())
arr = list(map(int,input().split()))

x, y = 0, 0
flag = True

for i in range(n-1, 0, -1):
    if arr[i] > arr[i-1]:
        x, y = i-1, i
        for j in range(n-1, 0, -1):
            if arr[j] > arr[x]:
                arr[j], arr[x] = arr[x], arr[j]
                flag = False
                break
    if flag == False:
        arr = arr[:y] + sorted(arr[y:])
        print(*arr)
        break

if flag == True:
    print(-1)
# https://jminie.tistory.com/76
