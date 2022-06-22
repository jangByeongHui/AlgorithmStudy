D,H,W = map(int,input().split())
R = D/((H**2)+(W**2))**0.5
print(int(R*H),int(R*W))
