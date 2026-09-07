T = int(input())
for tc in range(1, T+1):
    A, B = map(list, input().split())
    min_count = 0
    idx = 0

    while idx < len(A):
        if A[idx:idx+len(B)] == B:
            min_count += 1
            idx += len(B)

        else:
            min_count += 1
            idx += 1
    
    print(f'#{tc} {min_count}')
