from itertools import permutations
import sys

N = int(input())

numbers = list(map(int,input().split()))

answer = -sys.maxsize

for way in permutations(numbers):
    delta = 0

    for i in range(N-1):
        delta += abs(way[i]-way[i+1])
    answer = max(answer,delta)

print(answer)

