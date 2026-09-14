from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < 100 and 0 <= c < 100

def bfs(sr, sc):
    global result

    visited[sr][sc] = 1
    que = deque()
    que.append((sr, sc))

    while que:
        cr, cc = que.popleft()
        visited[cr][cc] = 1

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc

            if (nr, nc) == end:
                result = 1
                return

            if in_range(nr, nc) and maze[nr][nc] != '1' and not visited[nr][nc]:
                que.append((nr, nc))


for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    result = 0

    for r in range(100):
        for c in range(100):
            if maze[r][c] == '2':
                start = (r, c)
            if maze[r][c] == '3':
                end = (r, c)

    bfs(start[0], start[1])
    print(f'#{tc} {result}')

    