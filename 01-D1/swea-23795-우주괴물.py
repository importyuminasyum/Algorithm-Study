dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(input().split()) for _ in range(N)]
    result = 0
    # 시작점에서 광선이 뻗어나가면 '1'로 변경,
    # 마지막에 '0' 개수 세기
    for r in range(N):
        for c in range(N):
            if field[r][c] == '2':
                cr, cc = r, c

    for dr, dc in dirs:
        count = 0
        nr, nc = cr + dr, cc + dc

        while in_range(nr, nc) and field[nr][nc] != '1':
            field[nr][nc] = '1'
            nr, nc = nr + dr, nc + dc

    for r in range(N):
        result += field[r].count('0')

    print(f'#{tc} {result}')