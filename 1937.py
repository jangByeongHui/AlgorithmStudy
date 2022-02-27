import sys

N = int(sys.stdin.readline())
Number = list(map(int,sys.stdin.readline().split()))
Number.sort()
print(Number)
print(Number[0]*Number[-1])