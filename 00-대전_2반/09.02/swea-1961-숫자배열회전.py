def rotation_90(arr):
    rotated_arr = [
        [0] * N
        for _ in range(N)
    ]

    for row in range(N):
        for col in range(N):
            rotated_arr[col][N - row - 1] = arr[row][col]

    return rotated_arr

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    rotated90_arr = rotation_90(arr)
    rotated180_arr = rotation_90(rotated90_arr)
    rotated270_arr = rotation_90(rotated180_arr)

    print(f'#{tc}')
    for row in range(N):
        print(*rotated90_arr[row], sep='', end=' ')
        print(*rotated180_arr[row], sep='', end=' ')
        print(*rotated270_arr[row], sep='', end=' ')
        print()