import heapq

N = int(input())
queue = []

for _ in range(N):

    Numbers = list(map(int,input().split()))

    for number in Numbers:
        heapq.heappush(queue,number)

    while len(queue) > N:
        heapq.heappop(queue)

queue.sort()
print(queue[0])