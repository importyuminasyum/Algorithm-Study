def catch_flies(i, j):
    cul_sum = 0
    for row in range(i, i + M):
        for col in range(j, j + M):
            cul_sum += field[row][col]
    return cul_sum

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0

    field = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            result = max(result, catch_flies(i, j))

    print(f'#{tc} {result}')


