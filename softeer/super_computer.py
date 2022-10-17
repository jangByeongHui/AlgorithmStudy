import sys
from collections import defaultdict
input = sys.stdin.readline
# 데이터 입력
N, B = map(int,input().rstrip().split())
computers = list(map(int,input().rstrip().split()))

computers.sort()

left = 1
right = 2000000000
visited = defaultdict(bool)

while True:
    temp_buget = 0
    mid = int((left+right)//2)

    if visited[mid]:
        break
    visited[mid] = True

    for computer in computers:
        if mid > computer:
            temp_buget += (mid-computer)**2

    if temp_buget > B:
        right = mid

    elif temp_buget < B:
        left = mid
print(mid)



