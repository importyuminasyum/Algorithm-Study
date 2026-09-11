T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]

    center_idx = N // 2
    dist_range = N // 2

    profit = 0

    for r in range(N):
        for c in range(N):
            dist_from_center = abs(center_idx - r) + abs(center_idx - c)
            if dist_from_center <= dist_range:
                profit += field[r][c]

    print(f'#{tc} {profit}')