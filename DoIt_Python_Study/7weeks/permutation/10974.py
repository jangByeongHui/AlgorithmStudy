from itertools import permutations

N = int(input())

for way in permutations(range(1,N+1)):
    for element in way:
        print(element,end=" ")
    print()