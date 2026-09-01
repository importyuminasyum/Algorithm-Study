T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    result = []

    for i in range(N - M + 1):
        result.append(sum(A[i:i+M]))

    print(f'#{tc} {max(result) - min(result)}')