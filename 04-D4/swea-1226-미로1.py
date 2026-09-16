from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < 16 and 0 <= c < 16

def bfs():
    que = deque()
    que.append(start)
    maze[start[0]][start[1]] = '1'

    while que:
        cr, cc = que.popleft()

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc

            if not in_range(nr, nc):
                continue

            if maze[nr][nc] == '1':
                continue

            if maze[nr][nc] == '3':
                return 1

            que.append((nr, nc))
            maze[nr][nc] = '1'

    return 0

for _ in range(1, 11):
    tc = int(input())
    maze = [list(input()) for _ in range(16)]

    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                start = (r, c)

            if maze[r][c] == '3':
                end = (r, c)

    print(f'#{tc} {bfs()}')