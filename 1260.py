N,M,V=input().split()

N=int(N)
M=int(M)
V=int(V)

graph=[ [0 for _ in range(N)] for _ in range(N)]
visit=[0 for _ in range(N)]

Stack=list()
Queue=list()

def find_next(node):
    for i in range(N):
        if graph[node][i]==1 and visit[i]==0:
            return i
    return -1

for i in range(N):
    graph[i][i]=1

for i in range(M):
    s_node,t_node=input().split()
    s_node=int(s_node)-1
    t_node=int(t_node)-1
    graph[s_node][t_node]=1
    graph[t_node][s_node]=1

visit[V-1]=1
print(V,end=" ")

Stack.append(find_next(V-1))

while len(Stack)>0:
    temp_node=Stack.pop()
    if temp_node==-1:
        break
    visit[temp_node]=1
    print(temp_node+1,end=" ")

    next_node=find_next(temp_node)

    if next_node!=-1:
        Stack.append(next_node)
print()

for i in range(N):
    visit[i]=0

visit[V-1]=1   
print(V,end=" ")


for i in range(N):
    if graph[V-1][i] and visit[i]==0:
        Queue.append(i)

while len(Queue)>0:
    temp_node=Queue.pop(0)
    if visit[temp_node]==0:
        print(temp_node+1,end=" ")
        visit[temp_node]=1

    for i in range(N):
        if graph[temp_node][i] and visit[i]==0:
            Queue.append(i)
    




    
    







