from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    start_r, start_c = 0, 0
    end_r, end_c = N - 1, M - 1
    # visited[r][c] = 최소 거리
    visited = [
        [float('inf')] * M
        for _ in range(N)
    ]

    state = deque()
    state.append((start_r, start_c, 1, 0)) # 누적 길이, used가 k이기 전까지 벽 부수기 가능
    visited[0][0] = 0

    while state:
        cr, cc, length, used = state.popleft()

        if (cr, cc) == (end_r, end_c):
            return length

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc
            
            if not in_range(nr, nc):
                continue

            new_used = used

            if map_info[nr][nc] == '1':
                new_used += 1

            if new_used > K:
                continue

            if new_used < visited[nr][nc]:
                visited[nr][nc] = new_used
                state.append((nr, nc, length + 1, new_used))

    return -1

N, M, K = map(int, input().split())

map_info = [
    input()
    for _ in range(N)
]

print(bfs())