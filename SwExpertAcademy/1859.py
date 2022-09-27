
T = int(input())


for count in range(T):
    answer = 0
    days = int(input())
    days_price = list(map(int,input().split()))

    max_price = days_price[-1]

    for day in range(days-2,-1,-1):

        if days_price[day] >= max_price:
            max_price = days_price[day]
        else:
            answer += max_price - days_price[day]

    print(f"#{count+1} {answer}")