# 1인 곳만 배열 좌표 넣어서 탐색 시작
# 1인 곳 중에서도 방문하지 않은 배열만 bfs 시작
# 단지 count 증가
# 시작 좌표 que에 넣기
# 0이 아닌 곳, 방문하지 않은 곳에 대해서 que에 다시 넣고 그때 단지 count 배열의 집 count 증가

from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def bfs(cur_add):
    que = deque([cur_add])
    visited[cur_add[0]][cur_add[1]] = 1
    count = 1

    while que:
        cur_r, cur_c = que.popleft()

        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc

            if in_range(nr, nc, N) and not visited[nr][nc] and info[nr][nc]:
                visited[nr][nc] = 1
                que.append((nr, nc))
                count += 1

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
            complex_count.append(bfs((row, col)))

complex_count.sort()

print(len(complex_count))

for count in complex_count:
    print(count)
