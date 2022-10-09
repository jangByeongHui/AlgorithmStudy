n = int(input())

Q = [0,0,0,0,0]

for _ in range(n):
    x, y = map(int,input().split())

    if x == 0 or y == 0:
        Q[0] += 1
    elif x > 0 and y > 0:
        Q[1] += 1
    elif x < 0 and y > 0:
        Q[2] += 1
    elif x < 0 and y < 0:
        Q[3] += 1
    else:
        Q[4] += 1

print(f"Q1: {Q[1]}")
print(f"Q2: {Q[2]}")
print(f"Q3: {Q[3]}")
print(f"Q4: {Q[4]}")
print(f"AXIS: {Q[0]}")