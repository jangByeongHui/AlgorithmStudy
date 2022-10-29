# Algorithm Study
import sys

Front = 0
size = 0
T = int(sys.stdin.readline().rstrip())
que = [None] * T
Back = 0
for i in range(T):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == 'push':
        que[Back] = order[1]
        Back += 1
        if Back == T:
            Back = 0
        size += 1

    elif order[0] == 'pop':
        if size == 0:
            print(-1)
        else:
            print(que[Front])
            Front += 1
            if Front == T:
                Front = 0
            size -= 1

    elif order[0] == 'size':
        print(size)

    elif order[0] == 'empty':
        if size == 0:
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if size == 0:
            print(-1)
        else:
            print(que[Front])

    else:
        if size == 0:
            print(-1)
        else:
            temp = Back - 1
            print(que[temp])

