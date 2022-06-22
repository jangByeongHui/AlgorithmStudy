import queue

N=input()
N=int(N)

stone=list(map(int,input().split()))

Source,Target=input().split()
Source=int(Source)-1
Target=int(Target)-1

visit=[0 for _ in range(N)]
Queue=queue.Queue()
count=0
Queue.put((Source,count))


while Queue.empty()!=True:
    
    temp_pos,t_count=Queue.get()
    if visit[temp_pos]==0:
        visit[temp_pos]=1
        #print(temp_pos,t_count)
        if temp_pos==Target:
            print(t_count)
            break
        
        now_pos=temp_pos
        now_pos=temp_pos-stone[temp_pos]
        
        while 0<=now_pos:
            Queue.put((now_pos,t_count+1))
            now_pos=now_pos-stone[temp_pos]

        now_pos=temp_pos
        now_pos=now_pos+stone[temp_pos]

        while now_pos<N:
            Queue.put((now_pos,t_count+1))
            now_pos=now_pos+stone[temp_pos]

        
    else:
        continue
else:
    print(-1)
            



