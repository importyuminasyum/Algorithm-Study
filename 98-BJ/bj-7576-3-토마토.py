from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < M and 0 <= c < N

def bfs():    
    while queue:
        r, c = queue.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if in_range(nr, nc) and box[nr][nc] == 0:
                box[nr][nc] = box[r][c] + 1
                queue.append((nr, nc))

    for row in box:
        if 0 in row:
            return -1
        
    return box[r][c] - 1

N, M = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(M)
]

queue = deque()

for row in range(M):
    for col in range(N):
        if box[row][col] == 1:
            queue.append((row, col))

print(bfs())