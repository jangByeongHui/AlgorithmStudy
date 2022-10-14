from itertools import permutations

n = int(input())

number = list(map(int, input().split()))

plus, minus, multiple, divide = map(int, input().split())

operator = []

for _ in range(plus):
    operator.append("+")

for _ in range(minus):
    operator.append("-")

for _ in range(multiple):
    operator.append("*")

for _ in range(divide):
    operator.append("/")

min_value = 1000000000
max_value = -1000000000

for way in permutations(operator, n - 1):

    result = number[0]
    for op, value in zip(way, number[1:]):
        if op == "+":
            result += value
        elif op == "-":
            result -= value
        elif op == "/":
            if result < 0:
                result = abs(result)//value
                result = result*(-1)
            else:
                result //= value
        else:
            result *= value

    max_value = max(max_value, result)
    min_value = min(min_value, result)

print(max_value)
print(min_value)


