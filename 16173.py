
N=input()
N=int(N)
Stack=[]
Map=[]

visit=[[0 for _ in range(N)]for _ in range(N)]

for _ in range(N):
    Map.append(list(input().split()))

move=int(Map[0][0])
visit[0][0]=1
if move<N:
    Stack.append((move,0))
    Stack.append((0,move))

    while len(Stack)>0:

        i,j=Stack.pop()
        move=int(Map[i][j])
        visit[i][j]=1
        
        if i==N-1 and j==N-1:
            print("HaruHaru")
            break
        if N<=i or N<=j:
            print("Hing")
            
        if i+move<N:
            if visit[i+move][j]==0:
                Stack.append((i+move,j))
            
        if j+move<N:
            if visit[i][j+move]==0:
                Stack.append((i,j+move))
    else:
        print("Hing")
        

else:
    print("Hing")

        
