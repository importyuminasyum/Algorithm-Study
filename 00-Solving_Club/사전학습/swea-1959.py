T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    result = []
    total = 0

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N > M:
        N, M = M, N
        A, B = B, A
    
    for i in range(M - N + 1):
        for j in range(i, i + N):
            total += A[j-i] * B[j]
        result.append(total)
        total = 0

    print(f"#{test_case} {max(result)}")