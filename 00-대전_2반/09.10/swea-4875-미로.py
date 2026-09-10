dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(cur_r, cur_c):
    global result

    if result:
        return

    if (cur_r, cur_c) == end:
        result = 1
        return

    for dr, dc in dirs:
        nr, nc = cur_r + dr, cur_c + dc

        if in_range(nr, nc) and maze[nr][nc] in ('0', '3'):
            maze[nr][nc] = '1'
            dfs(nr, nc)

    return
    
T = int(input())
for tc in range(1, T+1):
    result = 0
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == '3':
                end = (r, c)
    
            if maze[r][c] == '2':
                start = (r, c)

    dfs(start[0], start[1])
    print(f'#{tc} {result}')