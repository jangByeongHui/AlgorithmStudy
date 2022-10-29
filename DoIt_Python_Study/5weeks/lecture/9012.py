# Algorithm Study

N = int(input())

for i in range(N):

    VPS = input()
    stack = []

    for v in VPS:
        if v == "(":
            stack.append(v)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:

        if not stack:
            print("YES")
        else:
            print("NO")