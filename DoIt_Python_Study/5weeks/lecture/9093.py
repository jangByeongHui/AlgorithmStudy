T = int(input())

for t in range(T):
    stack = []

    words = input().split()

    for word in words:

        for c in word:
            stack.append(c)

        while stack:
            print(stack.pop(),end="")
        print(end=" ")

    print()