import sys

N,K = map(int,sys.stdin.readline().rstrip().split())
coins=[]

for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=1)

init_pos=0
count = 0

while K>0 and init_pos<N:
    if K//coins[init_pos] > 0 :
        count+=K//coins[init_pos]
        K = K%coins[init_pos]
    else:
        init_pos+=1
print(count)