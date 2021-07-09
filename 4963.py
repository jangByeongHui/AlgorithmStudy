
def check_land(visit,Map,x,y,h,w):
    
    if Map[x][y]==1 and visit[x][y]==0:
        visit[x][y]=1
        Queue=list()

        Queue.append((x+1,y))
        Queue.append((x,y+1))
        Queue.append((x+1,y+1))

        while len(Queue)>0:
            t_X,t_Y=Queue.pop(0)
            
            if Map[t_X][t_Y]==1 and visit[t_X][t_Y]==0:
                visit[t_X][t_Y]=1
                if t_X==h and t_Y==w:
                    Queue.append((t_X+1,t_Y+1))
                    Queue.append((t_X+1,t_Y))
                    Queue.append((t_X,t_Y+1))

                elif t_X==0 and t_Y==w:
                    Queue.append((t_X+1,t_Y-1))
                    Queue.append((t_X+1,t_Y))
                    Queue.append((t_X,t_Y-1))
                elif t_X==h and t_Y==w:
                    Queue.append((t_X-1,t_Y-1))
                    Queue.append((t_X-1,t_Y))
                    Queue.append((t_X,t_Y-1))
                       
                else:
                    Queue.append((t_X,t_Y+1))
                    Queue.append((t_X+1,t_Y))
                    
                    Queue.append((t_X+1,t_Y+1))
                    Queue.append((t_X+1,t_Y-1))
                    Queue.append((t_X-1,t_Y-1))
                    Queue.append((t_X-1,t_Y+1))
        
        return True  
        
    else:
        return False
        
    



while True:
    w,h=map(int,input().split())

    if h==0 and w==0:
        break
    
    Map=list()
    visit=[[0 for _ in range(w)] for _ in range(h)]
    
    for _ in range(h):
        Map.append(list(map(int,input().split())))
        
    count=0

    for i in range(h):
        for j in range(w):
            if check_land(visit,Map,i,j,h-1,w-1)==True:
                count=count+1
    print(count)
    #print(visit)
    
    
            

    
