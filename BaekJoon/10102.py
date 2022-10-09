from collections import Counter
V = int(input())

vote = input()

vote_counter = Counter(vote)

if vote_counter['A'] > vote_counter['B']:
    print('A')
elif vote_counter['A'] < vote_counter['B']:
    print('B')
else:
    print('Tie')
