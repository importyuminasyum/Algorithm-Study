from itertools import combinations
from collections import deque
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def bfs():
    que = deque()

    for virus in viruses:
        que.append(virus)

    while que:
        x, y = que.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if in_range(nx, ny, N, M) and trial_map[nx][ny] == 0:
                que.append((nx, ny))
                trial_map[nx][ny] = 2

N, M = map(int, input().split())

max_safezone = 0

lab_map = [
    list(map(int, input().split()))
    for _ in range(N)
]

viruses, blank = [], []
for row in range(N):
    for col in range(M):
        if lab_map[row][col] == 2:
            viruses.append((row, col))
        if lab_map[row][col] == 0:
            blank.append((row, col))

for comb in combinations(blank, 3):
    trial_map = copy.deepcopy(lab_map)

    for wall_r, wall_c in comb:
        trial_map[wall_r][wall_c] = 1

    bfs()

    max_safezone = max(max_safezone, sum(row.count(0) for row in trial_map))

print(max_safezone)