'''
시작점 - 도착점까지 이동 가능 여부 판단
0 - 길 1 - 벽 2 - 출발점 3 - 도착점

출력 가능 1 불가능 0

dfs - 가능한 모든 동선 끝까지 확인

입력 T
maze
'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < 16 and 0 <= c < 16

def dfs(cr, cc):
    global result

    visited[cr][cc] = 1

    if result:
        return 

    if (cr, cc) == end:
        result = 1
        return

    for dr, dc in dirs:
        nr, nc = cr + dr, cc + dc

        if in_range(nr, nc) and maze[nr][nc] != '1' and not visited[nr][nc]:
            dfs(nr, nc)
            visited[nr][nc] = 0


for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    result = 0

    for r in range(16):
        for c in range(16):
            if maze[r][c] == '2':
                start = (r, c)
            if maze[r][c] == '3':
                end = (r, c)

    dfs(start[0], start[1])

    print(f'#{tc} {result}')