n = int(input())

player = [100,100]
for _ in range(n):
    first, second = map(int, input().split())

    if first > second:
        player[1] -= first
    elif first < second:
        player[0] -= second

for point in player:
    print(point)