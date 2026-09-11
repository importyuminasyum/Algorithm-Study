dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def check():
    global result 

    for r in range(N):
        for c in range(N):
            if result == 'YES':
                return

            if board[r][c] == 'o':
                cr, cc = r, c

                for dr, dc in dirs:
                    count = 0

                    for i in range(5):
                        nr, nc = cr + dr * i, cc + dc * i

                        if not in_range(nr, nc):
                            continue

                        if board[nr][nc] == 'o':
                            count += 1

                    if count == 5:
                        result = 'YES'
                        return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]

    result = 'NO'

    check()

    print(f'#{tc} {result}')