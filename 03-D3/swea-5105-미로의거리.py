from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs():
    que = deque()
    que.append(start)
    dist[start[0]][start[1]] = 0

    while que:
        cr, cc = que.popleft()

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc

            if not in_range(nr, nc):
                continue

            if maze[nr][nc] == '1':
                continue

            if maze[nr][nc] == '3':
                return dist[cr][cc]

            if dist[nr][nc]:
                continue

            que.append((nr, nc))
            dist[nr][nc] = dist[cr][cc] + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]
    dist = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if maze[r][c] == '2':
                start = (r, c)

            if maze[r][c] == '3':
                end = (r, c)

    print(f'#{tc} {bfs()}')