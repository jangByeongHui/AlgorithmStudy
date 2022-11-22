from itertools import combinations

while True:
    in_number = list(map(int,input().split()))

    if in_number[0] == 0:
        break

    for way in combinations(in_number[1:],6):
        for element in sorted(way):
            print(element,end=" ")
        print()
    print()
