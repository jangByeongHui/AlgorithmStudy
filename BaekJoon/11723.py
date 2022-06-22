import sys
M=int(sys.stdin.readline())

S=[]

while M>0:
    M-=1

    In = sys.stdin.readline()

    if "all" in In or "empty" in In:
        op=In
    else:
        op,num = In.split()
        num=int(num)

    if 'add' in op:
        if not num in S:
            S.append(num)

    elif "remove" in op:
        if num in S:
            S.remove(num)
    elif "check" in op:
        if num in S:
            print(1)
        else:
            print(0)

    elif "toggle" in op:
        if num in S:
            S.remove(num)
        else:
            S.append(num)

    elif "all" in op:
        S = [i for i in range(1,21)]

    elif "empty" in op:
        S = []