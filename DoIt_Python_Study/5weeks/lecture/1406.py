import sys

left_text = list(sys.stdin.readline().rstrip())
right_text = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())

    if command[0] == 'L':
        if left_text:
            right_text.append(left_text.pop())

    elif command[0] == 'D':
        if right_text:
            left_text.append(right_text.pop())

    elif command[0] == 'B':
        if left_text:
            left_text.pop()

    else:
        left_text.append(command[1])

left_text.extend(reversed(right_text))
print(''.join(left_text))