import queue

Queue = queue.Queue()
def print_table(List:list):
    m=len(List[0])
    n=len(List)
    for i in range(n):
        for j in range(m):
            print(List[i][j],end=" ")
        print()
#현재 위치에서 구할 수 있는 양과 늑대의 수를 구하는 함수
def find(map,table,t_sheep,t_wolf,i,j):
    if map[i][j] != '#' and table[i][j] == 0:
        table[i][j] = '.'
        if map[i][j] == 'k':
            t_sheep = t_sheep + 1
            table[i][j]='k'
        if map[i][j] == 'v':
            t_wolf = t_wolf + 1
            table[i][j] = 'v'
        # i,j 크기에 따라 상하좌우 탐색 조건
        if i < n-1 and j < m-1:
            Queue.put((i,j + 1))
            Queue.put((i + 1,j))
        if 0<i and 0<j:
            Queue.put((i - 1, j))
            Queue.put((i , j-1))
    elif table[i][j] == 0:
        table[i][j]='#'

    return (t_sheep,t_wolf)


if __name__=="__main__":
    n,m=input().split()
    n=int(n)
    m=int(m)
    Map=list()
    sheep=0
    wolf=0
    #방문했는지 안했는지 확인 방문하지 않았으면 0 ,방문했으면 그 위치에 값으로 변경
    search_table=temp=[[0 for _ in range(m)] for _ in range(n)]
    # 주어진 조건 입력
    for i in range(n):
        line=input()
        Map.append(line)

    for i in range(n):
        for j in range(m):
            t_wolf = 0
            t_sheep = 0

            #find 함수로 구한 양과 늑대 수(지금 울타리 안에서 살아있는 양과 늑대수)
            t_sheep,t_wolf=find(Map,search_table,t_sheep,t_wolf,i,j)

            while 0<Queue.qsize():
                t_i,t_j=Queue.get()
                t_sheep,t_wolf=find(Map,search_table,t_sheep,t_wolf,t_i,t_j)

            if t_wolf<t_sheep:
                sheep=sheep+t_sheep
            else:
                wolf=wolf+t_wolf
    ''' 탐색한 테이블 확인 '''
    #print_table(search_table)

    print(sheep,wolf)









