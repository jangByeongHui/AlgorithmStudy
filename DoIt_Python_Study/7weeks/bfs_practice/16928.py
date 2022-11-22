Map =[0 for _ in range(101)]
bfs =[]

N,M = map(int,input().split())

for _ in range(N+M):
    u,v=map(int,input().split())
    Map[u]=v

bfs.append((0,1))

while len(bfs)>0:
    count,now_pos = bfs.pop(0)
    # print((count,now_pos))
    if Map[now_pos]==-1:
        continue

    if 0<Map[now_pos]:
        now_pos=Map[now_pos]
        Map[now_pos]=-1

    if now_pos==100:
        print(count)
        break

    if now_pos+1<101:
        bfs.append((count+1,now_pos+1))
    if now_pos+2<101:
        bfs.append((count+1,now_pos+2))
    if now_pos+3<101:
        bfs.append((count+1,now_pos+3))
    if now_pos+4<101:
        bfs.append((count+1,now_pos+4))
    if now_pos+5<101:
        bfs.append((count+1,now_pos+5))
    if now_pos+6<101:
        bfs.append((count+1,now_pos+6))

    Map[now_pos]=-1