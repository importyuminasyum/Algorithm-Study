T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    result = 0

    if not B < C:
        result += B - (C - 1)
        B = C - 1

    if not A < B:
        result += A - (B - 1)
        A = B - 1

    if not A < B and not B < C or not (A and B and C):
        result = -1
        

    print(f'#{tc} {result}')
