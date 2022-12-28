n,m = map(int,input().split())

lecture_list = []

for _ in range(n):

    register, limit = map(int,input().split())
    mileage = list(map(int,input().split()))

    mileage.sort(reverse=True)

    if register >= limit:
        lecture_list.append(mileage[limit-1])
    else:
        lecture_list.append(1)

lecture_list.sort()
count = 0

for lecture in lecture_list:

    if lecture <= m:

        m -= lecture
        count += 1

    else:
        break

print(count)






