# k 범위: 배열의 1부터 최댓값 - 1 까지 순회 하면서
# 한 k에 대해서 물 잠기게 하기 - 0으로 바꾸기
# flood() - 원본 카피 행렬에 대해서 k 이하인 지점은 0으로 바꾸기
# 0이 아닌 좌표들 ground_rcs에 담기
# max_safe_zone = max(max_safe_zone, bfs(k))
# 각 시작 좌표를 넣고 bfs(k)
# 입력: k, 출력: 현 k에 대해서 안전 영역 개수 - safe_zone
# 누적 count: 현재 k에 대해서 안전한 영역의 개수
# k가 바뀔 때마다 방문 배열 초기화
# while que
# 한 for 돌때마다 count += 1 (안전한 영역)
# 방문 안 한 좌표만 que에 append
# count 누적

from collections import deque
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def bfs(k, cur_node, height_info):
    que = deque()
    que.append(cur_node)

    while que:
        cur_r, cur_c = que.popleft()

        if visited[cur_r][cur_c]:
            continue

        visited[cur_r][cur_c] = 1

        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc

            if in_range(nr, nc, N) and not visited[nr][nc] and height_info[nr][nc] > k:
                que.append((nr, nc))

N = int(input())

height_info = [
    list(map(int, input().split()))
    for _ in range(N)
]

max_safe_zone = 0

# 배열의 최댓값 검색 (k 범위 지정)
highest_height = 0
for row in range(N):
    highest_height = max(highest_height, max(height_info[row]))

for k in range(highest_height):
    safe_zone = 0
    visited = [
            [0] * N
            for _ in range(N)
        ]

    for row in range(N):
        for col in range(N):
            if height_info[row][col] > k and not visited[row][col]:
                bfs(k, (row, col), height_info)
                safe_zone += 1

    max_safe_zone = max(max_safe_zone, safe_zone)

print(max_safe_zone)