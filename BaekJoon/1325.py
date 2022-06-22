import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())



check=[[]for _ in range(N)]

result_count=[1 for _ in range(N)]

max_count=-1

for _ in range(M):
    A,B=map(int,input().split())

    check[B-1].append(A-1)

for i in range(N):

    count=0
    visit=[0 for _ in range(N)]
    Queue=deque()
    Queue.append(i)
    visit[i]=1    
    while len(Queue)>0:
        temp_N=Queue.popleft()

        for k in check[temp_N]:
            if visit[k]==0:
                visit[k]=1
                Queue.append(k)
                count=count+1

    
    if max_count<count:
        max_count=count
        
    if count!=0:
        result_count[i]=count

for i in range(N):
    if result_count[i]==max_count:
        #print(i+1,end=' ')
        sys.stdout.write(str(i+1)+' ')
        #sys.stdout.flush()
