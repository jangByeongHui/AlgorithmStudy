import sys
from itertools import combinations_with_replacement

scan = sys.stdin.readline

N,M = map(int,scan().rstrip().split())
NUM_LIST = list(map(int, scan().rstrip().split()))
NUM_LIST.sort()

if M==1:
    for i in NUM_LIST:
        print(i)
else:
    result = list(combinations_with_replacement(NUM_LIST,M))
    for i in result:
        for j in i:
            print(j,end=" ")
        print()

