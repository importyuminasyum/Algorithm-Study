dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 우 0 하 1 좌 2 상 3
dict = {1: (0, 1, 2, 3), 2: (1, 3), 3: (0, 2), 4: (0, 3), 5: (0, 1), 6: (1, 2), 7: (2, 3)}
connect = {0: 2, 1: 3, 2: 0, 3: 1}

# 내가 현재 있는 위치의 인덱스 값만 확인 
# 다음으로 보낼 위치의 터널 인덱스 값과 대칭되는지? 
# 지금 인덱스 값과 2 차이 나는 값이 다음 위치의 터널 인덱스 값 안에 있는지 확인

from collections import deque

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs():
    que = deque()
    que.append((R, C))

    visited[R][C] = 1
    count = 1
    t = 1

    while que:
        cr, cc = que.popleft()

        if visited[cr][cc] == L:
            continue

        for idx in dict[tunnel[cr][cc]]:
            dr, dc = dirs[idx]
            nr, nc = cr + dr, cc + dc

            if not in_range(nr, nc):
                continue

            if not tunnel[nr][nc]:
                continue

            if visited[nr][nc]:
                continue

            if not connect[idx] in dict[tunnel[nr][nc]]:
                continue

            visited[nr][nc] = visited[cr][cc] + 1
            count += 1
            que.append((nr, nc))

    return count

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    print(f'#{tc} {bfs()}')



    

