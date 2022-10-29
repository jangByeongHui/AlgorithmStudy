s = input()
answer = ''

for x in s:
    if 'a'<= x <='z':
        x=ord(x)+13

        if x > ord('z'):

            x -= 26

        answer += chr(x)

    elif 'A'<=x and x<='Z':

        x = ord(x)+13

        if x > ord('Z'):

            x -= 26

        answer += chr(x)
    else:
        answer += x

print(answer)