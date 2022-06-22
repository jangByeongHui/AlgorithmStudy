import sys

origin_str = sys.stdin.readline().rstrip()

bomb_str = sys.stdin.readline().rstrip()

bomb_lastChar = bomb_str[-1]

bomb_length = len(bomb_str)

stack = []


for char in origin_str:
    stack.append(char)

    if char == bomb_lastChar and ''.join(stack[-bomb_length:]) == bomb_str:
        del stack[-bomb_length:]

answer = "".join(stack)

if answer == "":
    print("FRULA")
else:
    print(answer)