import sys

N = int(sys.stdin.readline())

papers =[None for _ in range(N)]

for i in range(N):
    papers[i]=list(map(int,sys.stdin.readline().split()))

zero_count=0
minus_count=0
plus_count=0

for i in range(2,N):

