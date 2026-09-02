T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [
            [0] * 10
            for _ in range(10)
        ]
    
    purple = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
    
        for row in range(r1, r2 + 1):
            for col in range(c1, c2 + 1):
                if board[row][col] != 0 and board[row][col] != color:
                    purple += 1

                board[row][col] = color

    print(f'#{tc} {purple}')