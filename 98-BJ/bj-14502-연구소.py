# for comb in combinations(blanks, 3):
# for x, y in comb:
# (x, y)
# copy.deepcopy(map_shape)

from itertools import combinations
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(x, y, N, M):
    return 0 <= x < N and 0 <= y < M

def trial(comb):
    global max_safezone
    trial_map = copy.deepcopy(map_shape)
    
    for row, col in comb:
        trial_map[row][col] = 1

    for v_row, v_col in virus_rcs:
        virus_spread(trial_map, v_row, v_col)

    max_safezone = max(max_safezone, sum(row.count(0) for row in trial_map))

def virus_spread(trial_map, x, y):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if in_range(nx, ny, N, M) and trial_map[nx][ny] == 0:
            trial_map[nx][ny] = 2
            virus_spread(trial_map, nx, ny)

N, M = map(int, input().split())
map_shape = [
    list(map(int, input().split()))
    for _ in range(N)
]
max_safezone = float('-inf')

blank_rcs = []
virus_rcs = []

for row in range(N):
    for col in range(M):
        if map_shape[row][col] == 0:
            blank_rcs.append((row, col))
        elif map_shape[row][col] == 2:
            virus_rcs.append((row, col))

for comb in combinations(blank_rcs, 3):
    trial(comb)

print(max_safezone) 