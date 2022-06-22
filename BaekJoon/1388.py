
n,m=input().split()

n=int(n)
m=int(m)
stack=list()
count=0
visit=[[0 for _ in range(m)] for _ in range(n)]
map=[]
#맵 입력
for i in range(n):
    map.append(list(input()))
#같은 모양인데 방문하지 않았다면 방문으로 표시 최초 발견된 건 +1 추가
for i in range(n):
    for j in range(m):
        if map[i][j]=='-' and visit[i][j]==0:
            count=count+1
            visit[i][j]=1
            k=j+1
            while k<m and map[i][k]=='-' :
                visit[i][k]=1
                k=k+1
        if map[i][j]=='|' and visit[i][j]==0:
            count=count+1
            visit[i][j]=1
            k=i+1
            while k<n and map[k][j]=='|' :
                visit[k][j]=1
                k=k+1

print(count)





