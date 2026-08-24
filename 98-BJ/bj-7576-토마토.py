from collections import deque
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < M and 0 <= c < N

def ripe(trial_box, r, c):
    ripe_tomato = []
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if in_range(nr, nc) and trial_box[nr][nc] == 0:
            ripe_tomato.append((nr, nc))
            trial_box[nr][nc] = 1
    return ripe_tomato

def bfs():    
    trial_box = copy.deepcopy(box)
    state = deque(ripe_tomato_rcs)
    
    day = -1

    while state: 
        day += 1

        # 현재 depth로 들어간 만큼만 비우겠다
        for _ in range(len(state)):
            r, c = state.popleft()
            state.extend(ripe(trial_box, r, c))

    for row in trial_box:
        if 0 in row:
            return -1
        
    return day

N, M = map(int, input().split())
box = [
    list(map(int, input().split()))
    for _ in range(M)
]

ripe_tomato_rcs = []

for row in range(M):
    for col in range(N):
        if box[row][col] == 1:
            ripe_tomato_rcs.append((row, col))

print(bfs())