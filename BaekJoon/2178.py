import sys

N,M = map(int,sys.stdin.readline().split())
Map=[]
bfs=[]

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    temp_line=[]
    for i in range(len(line)):
        temp_line.append(int(line[i]))
    Map.append(temp_line)

bfs.append((0,0,1))

while 0<len(bfs):
    pos_x,pos_y,count = bfs.pop(0)
    #print(f'pos_x : {pos_x} pos_y : {pos_y} count :{count}')
    if pos_x==N-1 and pos_y ==M-1:
        record=count
        break

    if 0<pos_x and Map[pos_x-1][pos_y]==1:
        Map[pos_x-1][pos_y] = 2
        bfs.append((pos_x-1,pos_y,count+1))

    if pos_x<N-1 and Map[pos_x+1][pos_y]==1:
        Map[pos_x + 1][pos_y] = 2
        bfs.append((pos_x+1,pos_y,count+1))

    if 0<pos_y and Map[pos_x][pos_y-1]==1:
        Map[pos_x][pos_y-1] = 2
        bfs.append((pos_x,pos_y-1,count+1))

    if pos_y<M-1 and Map[pos_x][pos_y+1]==1:
        Map[pos_x][pos_y+1] = 2
        bfs.append((pos_x,pos_y+1,count+1))



#print(Map)
print(record)