from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    result = 0
    
    while que:
        cr, cc = que.popleft()

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc

            if not in_range(nr, nc):
                continue

            if dist[nr][nc] != -1:
                continue

            que.append((nr, nc))
            dist[nr][nc] = dist[cr][cc] + 1

            if arr[nr][nc] == 'L':
                result += dist[nr][nc]

    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dist = [[-1] * M for _ in range(N)]
    que = deque()

    for r in range(N):
        for c in range(M):
            if arr[r][c] == 'W':
                que.append((r, c))
                dist[r][c] = 0
    
    print(f'#{tc} {bfs()}')