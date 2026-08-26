dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상                                                                                                                                                                                                                                                                               

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def BFforce():
    

    for k in range(K + 1):
        for row in range(N):
            for col in range(N):
                map_info[row][col] -= k

                for sr, sc in start_rcs:
                    visited = [
                            [0] * N
                            for _ in range(N)
                        ]

                    dfs(1, sr, sc, visited)

                map_info[row][col] += k

def dfs(depth, sr, sc, visited):
    global max_length
    visited[sr][sc] = 1

    for dr, dc in dirs:
        nr, nc = sr + dr, sc + dc

        if in_range(nr, nc, N) and not visited[nr][nc] and map_info[nr][nc] < map_info[sr][sc]:
            visited[nr][nc] = 1
            dfs(depth + 1, nr, nc, visited)
            visited[nr][nc] = 0

        max_length = max(max_length, depth)


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    map_info = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    start_rcs = []
    highest_val = 0

    max_length = 0

    for row in range(N):
        highest_val = max(highest_val, max(map_info[row]))

    for row in range(N):
        for col in range(N):
            if map_info[row][col] == highest_val:
                start_rcs.append((row, col))

    BFforce()

    print(f'#{tc} {max_length}')