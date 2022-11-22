from collections import deque,defaultdict

N, K = map(int,input().split())

queue = deque([(N,0)])

visited = [-1]*100001
visited[N] = N

while queue:

    subin_n, subin_move = queue.popleft()

    if subin_n == K:
        path = []
        while subin_n != N:
            path.append(subin_n)
            subin_n = visited[subin_n]
        path.append(N)
        print(subin_move)
        print(*path[::-1])
        break

    if 0 <= subin_n+1 <= 100000 and visited[subin_n+1] == -1:
        queue.append((subin_n+1,subin_move+1))
        visited[subin_n+1] = subin_n

    if 0 <= subin_n-1 <= 100000 and visited[subin_n-1] == -1:
        queue.append((subin_n-1, subin_move + 1))
        visited[subin_n-1] = subin_n

    if 0 <= 2*subin_n <= 100000 and visited[2*subin_n] == -1:
        queue.append((2*subin_n, subin_move + 1))
        visited[2*subin_n] = subin_n
