import sys

N,M =map(int,sys.stdin.readline().rstrip().split())

edges=[[]for _ in range(N+1)]
check = [False for _ in range(N+1)]
dfs=[]
count = 0

for _ in range(M):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    edges[u].append(v)
    edges[v].append(u)

for i in range(1,N+1):
    if not check[i]:
        dfs.append(i)
        while len(dfs)>0:
            num = dfs.pop()
            check[num]=True
            for adj in edges[num]:
                if not check[adj]:
                    dfs.append(adj)
        count+=1

print(count)


