import sys

test_case=int(sys.stdin.readline())

for _ in range(test_case):
    n=int(sys.stdin.readline())
    categorylist=dict()


    for i in range(n):
        cloth, category = sys.stdin.readline().rstrip().split()
        try:
            categorylist[category]+=1
        except:
            categorylist[category]=0





