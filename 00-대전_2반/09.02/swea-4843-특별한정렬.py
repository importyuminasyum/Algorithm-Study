T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N - 1):
        if not i % 2: #짝수
            max_idx = i
            for j in range(i + 1, N):
                if A[j] > A[max_idx]: 
                    max_idx = j
            A[i], A[max_idx] = A[max_idx], A[i]

        else: # 홀수
            min_idx = i
            for j in range(i + 1, N):
                if A[j] < A[min_idx]: 
                    min_idx = j
            A[i], A[min_idx] = A[min_idx], A[i]

    A = A[:10]
    print(f'#{tc} {" ".join(map(str, A))}')