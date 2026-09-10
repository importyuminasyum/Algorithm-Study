'''
for idx in range(N - M + 1):
    for i in range(M):
        A[idx + i] * B[i]
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N < M:
        N, M = M, N
        A, B = B, A

    max_mul_sum = float('-inf')

    for offset in range(-(M - 1), N):
        mul_sum = 0

        for i in range(M):
            a_idx = offset + i
            if 0 <= a_idx < N:
                mul_sum += A[a_idx] * B[i]

        max_mul_sum = max(max_mul_sum, mul_sum)

    print(f'#{tc} {max_mul_sum}')