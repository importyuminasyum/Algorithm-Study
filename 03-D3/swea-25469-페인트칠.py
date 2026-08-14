T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    max_paint = max(H, W)
    min_paint = min(H, W)
    board = []
    paint = 0
    for i in range(H):
        board.append(list(input()))

    for i in range(min_paint):
        for j in range(max_paint):
            if board[i][j] != '#':
                break
        else:
            paint += 1

    if paint != min_paint:
        for i in range(max_paint):
            for j in range(min_paint):
                if board[i][j] != '#':
                    break
            else:
                paint += 1

    print(f'#{tc} {paint}')