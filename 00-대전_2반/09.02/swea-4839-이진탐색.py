def binary_search(goal, start, end, count):
    mid = (start + end) // 2

    if goal == mid:
        return count
    
    elif goal > mid:
        return binary_search(goal, mid, end, count + 1)

    else:
        return binary_search(goal, start, mid, count + 1)

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    if binary_search(A, 1, P, 1) < binary_search(B, 1, P, 1):
        result = 'A'
    elif binary_search(A, 1, P, 1) > binary_search(B, 1, P, 1):
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')