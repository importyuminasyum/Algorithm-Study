T = int(input())
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    T, C = [0] * N, [0] * N
    for i in range(N):
        T[i], C[i] = map(int, input().split())
        
    dp = [0] * (L + 1) # 현재까지 칼로리(인덱스)에 대해서 이 칼로리 이하일 때 최대 선호도
    for i in range(N):
        for c in range(L, C[i] - 1, -1):
            dp[c] = max(dp[c], dp[c - C[i]] + T[i])
        
    print(f'#{tc} {max(dp)}')