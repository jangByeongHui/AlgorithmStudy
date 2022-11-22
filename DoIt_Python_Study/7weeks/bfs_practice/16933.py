import collections
import sys


def bfs(cur_r, cur_c):
    q1, q2, q3 = collections.deque(), collections.deque(), collections.deque()
    q1.append([cur_r, cur_c, 0, 0])
    V[0][cur_r][cur_c] = 1
    while q1:
        while q1:
            cur_r, cur_c, time, brk = q1.popleft()
            depth = V[brk][cur_r][cur_c]
            if cur_r == N - 1 and cur_c == M - 1:
                return depth
            for dx, dy in dr:
                nxt_r, nxt_c = cur_r + dx, cur_c + dy
                if 0 <= nxt_r <= N - 1 and 0 <= nxt_c <= M - 1:
                    if A[nxt_r][nxt_c] == 1:
                        if time == 0 and brk < K and not V[brk + 1][nxt_r][nxt_c]:
                            q2.append([nxt_r, nxt_c, 1, brk + 1])
                            V[brk + 1][nxt_r][nxt_c] = depth + 1
                        elif time == 1 and brk < K and not V[brk + 1][nxt_r][nxt_c]:
                            q3.append([nxt_r, nxt_c, 1, brk + 1])
                            V[brk + 1][nxt_r][nxt_c] = depth + 2
                    elif A[nxt_r][nxt_c] == 0 and not V[brk][nxt_r][nxt_c]:
                        q2.append([nxt_r, nxt_c, (time + 1) % 2, brk])
                        V[brk][nxt_r][nxt_c] = depth + 1
        q1, q2, q3 = q2, q3, collections.deque()
        if not q1:
            q1, q2 = q2, collections.deque()
    return -1


N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline()[:-1])) for _ in range(N)]
V = [[[0] * M for _ in range(N)] for k in range(K + 1)]
dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
print(bfs(0, 0))