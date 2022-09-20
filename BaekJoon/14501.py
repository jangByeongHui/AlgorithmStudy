import sys

input = sys.stdin.readline

N = int(input().rstrip())

talks = []

for _ in range(N):
    talks.append(tuple(map(int,input().rstrip().split())))

print(talks)


