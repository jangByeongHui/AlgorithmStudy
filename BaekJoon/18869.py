from collections import defaultdict

M,N = map(int,input().split())

universal_weight = []
multi_universe_count = defaultdict(int)

for _ in range(M):

    # 우주마다 행성 랭크를 제한
    planets = list(map(int,input().split()))
    keys = sorted(list(set(planets))) # 랭크를 생성
    ranks = {keys[i]: i for i in range(len(keys))} # 행성 크기마다 최소 0부터 랭크를 부여
    add = tuple([ranks[x] for x in planets])
    multi_universe_count[add] += 1

answer = 0

# nC2 값으로 계산
for value in multi_universe_count.values():
    if value > 1:
        answer += value*(value-1)//2

print(answer)
