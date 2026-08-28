# 토마토 좌표 행렬 찾기
# [(면, 행, 열)]
# bfs():
# 토마토 좌표 행렬 큐에 넣기
# 큐에서 pop
# 현재 노드에 대해서 6방향 확인, 갈 수 있으면 가기 - 1. day 변수 지정 2. 이걸 방문배열이자 day로
# 종료시 남아있는 0이 있는지 확인, 있으면 -1, 없으면 day

from collections import deque

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
dirs = [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]

def in_range(z, r, c):
    return 0 <= z < H and 0 <= r < N and 0 <= c < M

def bfs():
    day = -1

    while ripe_tomato_rcs:
        day += 1

        for _ in range(len(ripe_tomato_rcs)):
            cz, cr, cc = ripe_tomato_rcs.popleft()

            for dz, dr, dc in dirs:
                nz, nr, nc = cz + dz, cr + dr, cc + dc

                if in_range(nz, nr, nc) and not box[nz][nr][nc]:
                    box[nz][nr][nc] = 1
                    ripe_tomato_rcs.append((nz, nr, nc))

    for h in range(H):
        for r in range(N):
            if 0 in box[h][r]:
                return -1
    return day

M, N, H = map(int, input().split())

box = [[
    list(map(int, input().split()))
    for _ in range(N)
] for _ in range(H)
]

ripe_tomato_rcs = deque()

for z in range(H):
    for r in range(N):
        for c in range(M):
            if box[z][r][c] == 1:
                ripe_tomato_rcs.append((z, r, c))

print(bfs())