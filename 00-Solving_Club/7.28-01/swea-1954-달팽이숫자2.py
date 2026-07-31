dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    dir = 0
    x, y = 0, 0

    arr = [[ 0 for i in range(N)] for _ in range(N)] 
    arr[x][y] = 1

    for i in range(2, N * N + 1):
        nx, ny = x + dxs[dir], y + dys[dir]

        if not in_range(nx, ny, N) or arr[nx][ny] != 0:
            dir = (dir + 1) % 4

        x, y = x + dxs[dir], y + dys[dir]
        arr[x][y] = i

    print(f'#{test_case}')
    for i in range(N):
        print(*arr[i])
