def P(N):
    if N <= 3:
        return 1

    return P(N - 3) + P(N - 2)

T = int(input())
for tc in range(1, T + 1):
    p = [0, 1, 1]
    N = int(input())
    for i in range(3, N + 1):
        p.append(p[i - 3] + p[i - 2])

    print(f'#{tc} {p[N]} {P(N)}') # dp / 재귀