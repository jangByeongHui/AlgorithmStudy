# Algorithm Study
import sys

Top = 0

T = int(sys.stdin.readline().rstrip())
Stack = [None] * T

for i in range(T):
    order = sys.stdin.readline().rstrip().split()

    if order[0] == 'push':
        Stack[Top] = order[1]
        Top += 1

    elif order[0] == 'pop':
        if Top == 0:
            print(-1)
        else:
            Top -= 1
            print(Stack[Top])

    elif order[0] == 'size':
        print(Top)

    elif order[0] == 'empty':
        if Top == 0:
            print(1)
        else:
            print(0)

    else:
        if Top == 0:
            print(-1)

        else:
            temp = Top - 1
            print(Stack[temp])

