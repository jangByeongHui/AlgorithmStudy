import queue
import sys
input = sys.stdin.readline
N=int(input())

for _ in range(N):

    l=int(input())

    s_X,s_Y=map(int,input().split())

    t_X,t_Y=map(int,input().split())

    #print(s_X,s_Y,t_X,t_Y)

    visit=[[0 for _ in range(l)] for _ in range(l)]

    Queue=queue.Queue()
    Queue.put((s_X,s_Y,0))
    count=0
    while Queue.empty()!=True:
        temp_X,temp_Y,t_count=Queue.get()
        #print(count)
        count=count+1
        if visit[temp_X][temp_Y]==1:
            continue
        visit[temp_X][temp_Y]=1
        #print(temp_X,temp_Y,visit[temp_X][temp_Y],t_count,t_X,t_Y)
        if temp_X==t_X and temp_Y==t_Y:
            print(t_count)
            break

        if 0<temp_X and 1<temp_Y and visit[temp_X-1][temp_Y-2]==0:
                Queue.put((temp_X-1,temp_Y-2,t_count+1))

        if 1<temp_X and 0<temp_Y and visit[temp_X-2][temp_Y-1]==0:
                Queue.put((temp_X-2,temp_Y-1,t_count+1))

        if 1<temp_X and temp_Y<l-1 and visit[temp_X-2][temp_Y+1]==0:
                Queue.put((temp_X-2,temp_Y+1,t_count+1))

        if 0<temp_X and temp_Y<l-2 and visit[temp_X-1][temp_Y+2]==0:
                Queue.put((temp_X-1,temp_Y+2,t_count+1))
                    
        if temp_X<l-1 and temp_Y<l-2 and visit[temp_X+1][temp_Y+2]==0:
                Queue.put((temp_X+1,temp_Y+2,t_count+1))
                    
        if temp_X<l-2 and temp_Y<l-1 and visit[temp_X+2][temp_Y+1]==0:
                Queue.put((temp_X+2,temp_Y+1,t_count+1))
                    
        if temp_X<l-2 and 0<temp_Y and visit[temp_X+2][temp_Y-1]==0:
                Queue.put((temp_X+2,temp_Y-1,t_count+1))
                    
        if temp_X<l-1 and 1<temp_Y and visit[temp_X+1][temp_Y-2]==0:
                Queue.put((temp_X+1,temp_Y-2,t_count+1)) 
            
    else:
        print(0)
