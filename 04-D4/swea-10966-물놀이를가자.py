from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    global min_move

    while water_rcs:
        cr, cc = water_rcs.popleft()
        
        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc 

            if not in_range(nr, nc):
                continue

            if dist[nr][nc] >= 0:
                continue

            dist[nr][nc] = dist[cr][cc] + 1

            if map_info[nr][nc] == 'L':
                min_move += dist[nr][nc]

            water_rcs.append((nr, nc))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    map_info = [input() for _ in range(N)]
    water_rcs = deque()
    dist = [[-1] * M for _ in range(N)]
    min_move = 0

    for r in range(N):
        for c in range(M):
            if map_info[r][c] == 'W':
                water_rcs.append((r, c))
                dist[r][c] = 0

    bfs()
    print(f'#{tc} {min_move}')