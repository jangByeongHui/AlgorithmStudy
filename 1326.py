import queue

N=input()
N=int(N)

stone=list(map(int,input().split()))

Source,Target=input().split()
Source=int(Source)
Target=int(Target)

visit=[0 for _ in range(N)]
Queue=queue.Queue()

Queue.put(Source)

while len(Queue)>0:
    temp_pos=Queue.get()
    if visit[temp_pos]==0:
        visit[temp_pos]=1
        
        diff=abs(Target-Source)
        move=diff//stone[temp_pos]

        if Source<Target and Source+move<N:
            while
        if Target<Source and 0<(Source-move):
            Source=Source-move
            Queue.put(Source)
    el




