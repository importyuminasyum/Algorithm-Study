from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < M and 0 <= c < N

def bfs():    
    day = -1
    
    while ripe_tomato_rcs:
        cur_tomato = len(ripe_tomato_rcs)
        day += 1
        for _ in range(cur_tomato):
            r, c = ripe_tomato_rcs.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if in_range(nr, nc) and box[nr][nc] == 0:
                    box[nr][nc] = 1
                    ripe_tomato_rcs.append((r, c))

    for row in box:
        if 0 in row:
            return -1
        
    return day

N, M = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(M)
]

ripe_tomato_rcs = deque()

for row in range(M):
    for col in range(N):
        if box[row][col] == 1:
            ripe_tomato_rcs.append((row, col))

print(bfs())