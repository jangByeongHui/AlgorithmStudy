N = int(input())

vote = [0,0]

for _ in range(N):
    vote[int(input())] += 1

if vote[0] >= vote[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")