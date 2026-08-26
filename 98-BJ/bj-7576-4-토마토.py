# bfs로 탐색, 시작점 - 토마토 좌표를 모두 큐에 넣고 빼면서 상하좌우 탐색해서 토마토 익히기
# 상자 안 토마토가 익게 되는 최소 일수, 불가능하다면 -1
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c, N, M):
    return 0 <= r < N and 0 <= c < M

def bfs():
    while tomato_rcs:

        cr, cc = tomato_rcs.popleft()

        for dr, dc in dirs:
            nr, nc = cr + dr, cc + dc 

            if in_range(nr, nc, N, M) and not box[nr][nc]:
                box[nr][nc] = box[cr][cc] + 1
                tomato_rcs.append((nr, nc))

    for row in box:
        if 0 in row:
            return -1

    return box[cr][cc] - 1

M, N = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(N)
]

tomato_rcs = deque()
for row in range(N):
    for col in range(M):
        if box[row][col] == 1:
            tomato_rcs.append((row, col))

print(bfs())