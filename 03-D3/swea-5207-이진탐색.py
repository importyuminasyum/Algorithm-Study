def binary_search(left, right, b_value, prev):
    global count

    if left > right:
        return

    m = (left + right) // 2 # 중간 값 인덱스

    if A[m] == b_value:
        count += 1
        return

    elif A[m] > b_value:
        choice = 0
        if choice == prev:
            return
        binary_search(left, m - 1, b_value, choice)
        
    else:
        choice = 1
        if choice == prev:
            return
        binary_search(m + 1, right, b_value, choice)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    count = 0 # 결과

    for b in B:
        binary_search(0, len(A) - 1, b, -1)

    print(f'#{tc} {count}')