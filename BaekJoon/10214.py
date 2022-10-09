T = int(input())

for _ in range(T):
    scores = {'Y':0,"K":0}

    for g in range(9):
        y, k = map(int,input().split())

        scores['Y'] += y
        scores['K'] += k

    if scores['Y'] > scores['K']:
        print("Yonsei")
    elif scores['Y'] < scores['K']:
        print("Korea")
    else:
        print("Draw")