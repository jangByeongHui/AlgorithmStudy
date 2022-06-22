l = int(input())

r = int(input())

k = int(input())

count = 0

if k == 2:
    count = max(r-max(l,3)+1,0)

elif k == 3:

    for i in range(max(l,6),r+1,1):
        if i % 3 == 0:
            count += 1


elif k == 4:
    for i in range(max(l,10), r + 1, 1):
        if i % 2 == 0 and i!=12:
            count += 1


elif k == 5:
    for i in range(max(l,15), r + 1, 1):
        if i % 5 == 0:
            count += 1

print(count)