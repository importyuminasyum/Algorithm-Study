dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    snail = [
        [0] * N
        for _ in range(N)
    ]
    r, c, dir = 0, 0, 0

    for idx in range(1, N ** 2 + 1):
        snail[r][c] = idx

        nr, nc = r + dr[dir], c + dc[dir]

        if not in_range(nr, nc, N) or snail[nr][nc]:
            dir = (dir + 1) % 4
            nr, nc = r + dr[dir], c + dc[dir]

        r, c = nr, nc
    
    print(f'#{tc}')
    for i in range(N):
        print(*snail[i])