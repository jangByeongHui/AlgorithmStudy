from collections import Counter

T = int(input())

for _ in range(T):

    index = int(input())

    counter = Counter(list(map(int,input().split())))

    print(f"#{index} {counter.most_common(1)[0][0]}")