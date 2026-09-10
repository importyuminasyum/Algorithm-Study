'''
N: 행, M: 열
땅으로 표현된 모든 칸에서 어떤 물 칸으로 이동하기 위한 최소 횟수를 구하고, 모든 이동 횟수의 합 출력

일단 물들을 시작점으로 잡고, 
땅을 발견할 때마다 걔가 갖고 있는 move를 result에 누적하기
방문 처리
그런데 다른 시작점에서 시작한다면 먼저 도착하는 애가 무조건 최소경로임
땅을 발견했다면 그때의 이동횟수를 누적하고 계속 가 

'''
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def land_search():
    result = 0
    visited = [[0] * M for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    move = 0

    while water_rcs:
        cur_r, cur_c = water_rcs.popleft()
        visited[cur_r][cur_c] = 1

        for dr, dc in dirs:
            nr, nc = cur_r + dr, cur_c + dc

            if not in_range(nr, nc):
                continue

            if field[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = 1

                dist[nr][nc] = dist[cur_r][cur_c] + 1
                result += dist[nr][nc] + 1
                
                water_rcs.append((nr, nc))

    return dist

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [
        input()
        for _ in range(N)
    ]

    water_rcs = deque()
    for r in range(N):
        for c in range(M):
            if field[r][c] == 'W':
                water_rcs.append((r, c))

    print(f'#{tc} {land_search()}') 