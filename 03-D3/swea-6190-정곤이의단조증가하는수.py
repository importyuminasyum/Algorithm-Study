def non_decreasing_check(num):
    a = num % 10
    i = 0
    while i != N - 1:
        num //= 10
        b = num % 10
        
        if a < b:
            return False

        a = num % 10
        i += 1

    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)

    max_num = float('-inf')
    for i in range(N - 1):
        for j in range(i + 1, N):
            num = A[i] * A[j]
            if num < max_num:
                continue

            if non_decreasing_check(num):
                max_num = max(max_num, num)

    if max_num == float('-inf'):
        max_num = -1

    print(f'#{tc} {max_num}')