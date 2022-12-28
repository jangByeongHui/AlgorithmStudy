A,B,G = map(int,input().split())

team_A = set(list(input().split()))
team_B = set(list(input().split()))

score_A = 0
score_B = 0

goal_players = list(input().split())

for player in goal_players:

    if player in team_A:
        score_A += 1
    else:
        score_B += 1

if score_A > score_B:
    print("A")
elif score_B > score_A:
    print("B")
else:
    print("TIE")

