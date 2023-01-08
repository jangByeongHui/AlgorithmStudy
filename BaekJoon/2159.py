import sys
from collections import deque

dir = [(0,1),(1,0),(0,-1),(-1,0)]

N = int(input())

sun_a_x, sun_a_y = map(int,input().split())
sun_a = {"x":sun_a_x,"y":sun_a_y}
people_pos_list = deque()



for _ in range(N):

    candidate_pos = []
    person_x, person_y = map(int,input().split())

    candidate_pos.append((person_x,person_y))

    for dx, dy in dir:
        if 0 <= person_x + dx < 100000 and 0 <= person_y + dy < 100000:
            candidate_pos.append((person_x+dx,person_y+dy))

    people_pos_list.append(candidate_pos)


answer = sys.maxsize

def dfs(count,x,y,dis):

    global answer

    if count >= N:
        answer = min(answer,dis)
        return dis

    for dx, dy in people_pos_list[count]:

        dfs(count+1,dx,dy,dis+abs(x-dx)+abs(y-dy))

dfs(0,sun_a_x,sun_a_y,0)

print(answer)

