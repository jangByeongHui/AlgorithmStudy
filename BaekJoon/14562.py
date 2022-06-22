n=int(input())
result=list()


for _ in range(n):
    S,T=map(int,input().split())
    Queue=list()

    Queue.append((0,S,T))
    
    while len(Queue)>0:
        t_count,t_S,t_T=Queue.pop(0)
        if t_S==t_T:
            result.append(t_count)
            break
        if t_T<t_S:
            continue

        else:
            
            Queue.append((t_count+1,t_S+t_S,t_T+3))
            Queue.append((t_count+1,t_S+1,t_T))
            

for i in result:
    print(i)
