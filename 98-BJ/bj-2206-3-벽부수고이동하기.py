from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs(r, c):
    min_length = 1
    visited[r][c][1] = 1
    state = deque([(r, c, 1)])

    while state:
        for _ in range(len(state)):
            r, c, chance = state.popleft()

            if (r, c) == (N - 1, M - 1):
                return visited[r][c][chance]

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if in_range(nr, nc):
                    if grid[nr][nc] == 1:
                        if chance == 1 and not visited[nr][nc][0]: # 기회를 쓰는 지점 
                            # 벽을 부순 적이 없는 상태로 그 칸을 방문했는지?
                            visited[nr][nc][0] = visited[r][c][chance] + 1 # 방문체크 + 거리
                            state.append((nr, nc, 0))

                    elif grid[nr][nc] == 0:
                        if not visited[nr][nc][chance]:
                            visited[nr][nc][chance] = visited[r][c][chance] + 1 # 방문체크
                            state.append((nr, nc, chance))
    return -1    

N, M = map(int, input().split()) # 종료지점

visited = [ [ [0] * 2 for _ in range(M) ] for _  in range(N) ]
# visited[r][c][1]
# 벽을 아직 부수지 않은 상태로 (r, c)에 도착한 거리

# visited[r][c][0]
# 벽을 이미 부순 상태로 (r, c)에 도착한 거리

grid = [
    list(map(int, input()))
    for _ in range(N)
]

print(bfs(0, 0))