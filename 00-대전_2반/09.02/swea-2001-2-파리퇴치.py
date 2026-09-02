T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0

    field = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    prefix = [
        [0] * (N + 1)
        for _ in range(N + 1)
    ]

    for row in range(N):
        for col in range(N):
            prefix[row + 1][col + 1] = field[row][col] + prefix[row + 1][col] + prefix[row][col + 1] - prefix[row][col]

    for row in range(M, N + 1):
        for col in range(M, N + 1):
            result = max(result, prefix[row][col] - prefix[row - M][col] - prefix[row][col - M] + prefix[row - M][col - M])
            
    print(f'#{tc} {result}')