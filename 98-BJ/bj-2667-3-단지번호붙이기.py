# 1인 곳만 배열 좌표 넣어서 탐색 시작
# 1인 곳 중에서도 방문하지 않은 배열만 dfs 시작
# visited 배열 공유

from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def dfs(cur_add):
    global count

    cur_r, cur_c = cur_add[0], cur_add[1]
    visited[cur_r][cur_c] = 1
    count += 1

    for dr, dc in dirs:
        nr, nc = cur_r + dr, cur_c + dc 

        if in_range(nr, nc, N) and not visited[nr][nc] and info[nr][nc]:
            dfs((nr, nc))

    return count

N = int(input())

info = [
    list(map(int, input()))
    for _ in range(N)
]

complex_count = [] # 길이: 단지 개수, 값: 각 인덱스 + 1 번지 단지에 대한 count

visited = [
        [0] * N
        for _ in range(N)
    ]

for row in range(N):
    for col in range(N):
        if info[row][col] and not visited[row][col]:
            count = 0
            complex_count.append(dfs((row, col)))

complex_count.sort()

print(len(complex_count))

for count in complex_count:
    print(count)
