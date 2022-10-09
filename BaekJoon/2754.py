grade = input()

def point(grade,result):

    if "+" in grade:
        result += 0.3
    elif "-" in grade:
        result -= 0.3
    return result

if "A" in grade:
    print(point(grade,4.0))
elif "B" in grade:
    print(point(grade, 3.0))
elif "C" in grade:
    print(point(grade, 2.0))
elif "D" in grade:
    print(point(grade, 1.0))
else:
    print(0.0)