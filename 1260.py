N,M,V=input().split()

N=int(N)
M=int(M)
V=int(V)

graph=[ [0 for _ in range(N)] for _ in range(N)]
visit=[0 for _ in range(N)]

Stack=list()
Queue=list()

def BFS(root):
    Queue.append(root)
    result=list()
    while len(Queue)>0:
        temp_node=Queue.pop(0)
        if visit[temp_node]==0:
            result.append(temp_node+1)
            visit[temp_node]=1
        
        for i in range(N):
            if graph[temp_node][i]==1 and visit[i]==0:
                Queue.append(i)
    
    return result

def DFS(root):
    Stack.append(root)
    result=list()

    while len(Stack)>0:
        temp_node=Stack.pop()
        if visit[temp_node]==0:
            result.append(temp_node+1)
            visit[temp_node]=1
        for i in reversed(range(N)):
            if graph[temp_node][i]==1 and visit[i]==0:
                Stack.append(i)
    return result


for i in range(N):
    graph[i][i]=1

for i in range(M):
    s_node,t_node=input().split()
    s_node=int(s_node)-1
    t_node=int(t_node)-1
    graph[s_node][t_node]=1
    graph[t_node][s_node]=1

#DFS
DFS_Answer=DFS(V-1)

for i in DFS_Answer:
    print(i,end=" ")

print()

for i in range(N):
    visit[i]=0

# BFS
BFS_Answer=BFS(V-1)
for i in BFS_Answer:
    print(i,end=" ")
    




    
    







