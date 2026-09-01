T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    cur_value = sum(A[:3])
    print(cur_value)
    max_value, min_value = cur_value, cur_value

    for i in range(N - M):
        cur_value += A[i + 3] - A[i]
        max_value = max(cur_value, max_value)
        min_value = min(cur_value, min_value)

    print(f'#{tc} {max_value - min_value}')