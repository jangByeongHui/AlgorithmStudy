import queue

def print_table(List:list):
    m=len(List[0])
    n=len(List)
    for i in range(n):
        for j in range(m):
            print(List[i][j],end=" ")
        print()


def make_Table(n:int,m:int):
    temp=[[0 for _ in range(m)] for _ in range(n)]
    return temp


if __name__=="__main__":
    n,m=input().split()
    n=int(n)
    m=int(m)
    Queue=queue()
    map=list()
    search_table=make_Table(n,m)

    for i in range(n):
        line=input()
        map.append(line)

    for i in range(n):
        for j in range(m):
            if map[i][j]=='O':

