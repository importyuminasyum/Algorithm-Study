# 알고리즘: 숫자에 대해서 정렬 후 그 인덱스에 대해서 정렬 해야 하는 swap들의 차?
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A, B = [], []
    swap = 0

    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    for i in range(N):
        for j in range(i + 1, N):
            if (A[i] > A[j] and B[i] < B[j]) or (A[i] < A[j] and B[i] > B[j]):
                swap += 1

    print(f'#{tc} {swap}')