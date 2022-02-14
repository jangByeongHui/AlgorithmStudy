import sys

N = int(sys.stdin.readline())
dp=[]


people= list(map(int,sys.stdin.readline().split()))

people.sort()

dp.append(people[0])

for i in range(1,N):
    dp.append(people[i]+dp[i-1])

sum=0

for i in dp:
    sum+=i

print(sum)