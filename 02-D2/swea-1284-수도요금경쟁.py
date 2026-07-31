t = int(input())
for test_case in range(1, t + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if P <= R:
        B = Q
    else:
        B = Q + S * (W - R)
    print(f'#{test_case} {min(A, B)}')