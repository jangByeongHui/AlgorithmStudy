N = int(input())
answer = -1

for _ in range(N):

    first, second, third = map(int,input().split())

    if first == second and second == third:
        answer = max(answer,10000+(first*1000))

    elif first == second:
        answer = max(answer,1000+(first*100))

    elif second == third:
        answer = max(answer,1000+(second*100))

    elif first == third:
        answer = max(answer,1000+(first*100))

    else:
        max_number = max(first,second,third)
        answer = max(answer,max_number*100)

print(answer)