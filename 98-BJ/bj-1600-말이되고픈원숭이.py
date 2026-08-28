from collections import deque

monkey = [(0, 1), (1, 0), (0, -1), (-1, 0)]
horse = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)] # 우상부터 시작

def in_range(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def bfs():
    global min_move
    que = deque()
    que.append((0, 0, 0))
    visited[0][0][0] = 1
    
    while que:
        r, c, used = que.popleft()

        if (r, c) == (H - 1, W - 1):
            return visited[used][r][c] - 1
        
        if used < K:
            # 말 가능
            for hr, hc in horse:
                nr, nc = r + hr, c + hc
                # 인덱스 범위 내이고, 다음 횟수에 대해서 방문한 적 없고, 장애물이 아닐 때
                if in_range(nr, nc, H, W) and not visited[used + 1][nr][nc] and not field[nr][nc]:
                    visited[used + 1][nr][nc] = visited[used][r][c] + 1
                    que.append((nr, nc, used + 1))

        # 원숭이 가능
        for mr, mc in monkey:
            nr, nc = r + mr, c + mc
            # 인덱스 범위 내이고, 이번 횟수에 대해서 방문한 적 없고, 장애물이 아닐 때
            if in_range(nr, nc, H, W) and not visited[used][nr][nc] and not field[nr][nc]:
                visited[used][nr][nc] = visited[used][r][c] + 1
                que.append((nr, nc, used))

    return -1

K = int(input())
W, H = map(int, input().split())
field = [
    list(map(int, input().split()))
    for _ in range(H)
]

min_move = float('inf')
visited = [[
    [0] * W
    for _ in range(H)]
    for _ in range(K + 1)
]

print(bfs())