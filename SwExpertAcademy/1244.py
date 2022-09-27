C = int(input())

def dfs(index,count):
    global answer

    N = len(target)

    if count == swap_count:
        answer = max(answer, int("".join(target)))
        return

    if "".join(target) in result[count]:
        return

    result[count].append("".join(target))

    for i in range(index,N):
        for j in range(i+1,N):
            target[i], target[j] = target[j], target[i]
            dfs(i,count+1)
            target[i], target[j] = target[j], target[i]

for c in range(C):

    target, swap_count = input().split()
    swap_count = int(swap_count)

    result = [[] for _ in range(swap_count+1)]

    answer = 0

    target = list(target)

    dfs(0,0)

    print(f"#{c+1} {answer}")