T = int(input())

A, B, C = 0, 0, 0

A = T//300
T = T % 300

B = T // 60
T = T % 60

if T//10 >= 0 and T % 10 == 0:
    print(A,B,T//10)
else:
    print(-1)