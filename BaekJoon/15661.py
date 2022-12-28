import sys
from itertools import combinations

N = int(input())

S = []

for _ in range(N):
    S.append(list(map(int,input().split())))

members = [i for i in range(N)]


def calculate_weight(team_members):

    score = 0
    for member in team_members:

        for other_member in team_members:
            if other_member == member:
                continue
            score += S[member][other_member]

    return score

result = sys.maxsize

for n in range(1,N):
    for team_A_members in combinations(members,n):
        team_B_members = [i for i in members if i not in set(team_A_members)]
        team_A = calculate_weight(team_A_members)
        team_B = calculate_weight(team_B_members)

        result = min(result,abs(team_A-team_B))

print(result)