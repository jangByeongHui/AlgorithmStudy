import sys
from collections import deque
import gc

input=sys.stdin.readline

N,M=map(int,input().split())

check=[[]for _ in range(N)]

result_count=[0 for _ in range(N)]
max_count=-1

for _ in range(M):
    A,B=map(int,input().split())

    check[B-1].append(A-1)
    
for i in range(N):

    count=0

    visit=[False for _ in range(N)]

    Queue=deque()
    
    Queue.append(i)
    
    while len(Queue)>0:
        temp_N=Queue.popleft()

        for k in check[temp_N]:
            if visit[k]==False:
                visit[k]=1
                Queue.append(k)
                count=count+1              
            
    if max_count<count:
        max_count=count

    result_count[i]=count
    

#for i in range(N):
#    print(check[i])


for i in range(N):
    if result_count[i]==max_count:
        print(i+1,end=' ')
        
        
