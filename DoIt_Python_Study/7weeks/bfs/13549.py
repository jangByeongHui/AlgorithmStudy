from collections import deque,defaultdict

N, K = map(int,input().split())

queue = deque([(N,0)])
visited = defaultdict(bool)

while queue:

    subin_n, subin_move = queue.popleft()

    if subin_n == K:
        print(subin_move)
        break

    if visited[subin_n]:
        continue

    visited[subin_n] = True

    if 0 <= subin_n+1 <= 100000:
        queue.append((subin_n+1,subin_move+1))

    if 0 <= subin_n-1 <= 100000:
        queue.append((subin_n-1, subin_move + 1))

    if 0 <= 2*subin_n <= 100000:
        queue.appendleft((2*subin_n, subin_move))


