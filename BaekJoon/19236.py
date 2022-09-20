import sys
input = sys.stdin.readline


directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
# 데이터 입력
fish_ball = []
fish_pos = dict()

for row in range(4):
    fishes = list(map(int,input().rstrip().split()))
    fish_ball.append([[fishes[0],fishes[1]],[fishes[2],fishes[3],row,1],[fishes[4],fishes[5]],[fishes[6],fishes[7]]])
    fish_pos[fishes[0]] = [row,0]
    fish_pos[fishes[2]] = [row,1]
    fish_pos[fishes[4]] = [row,2]
    fish_pos[fishes[6]] = [row,3]


