def dfs(idx, price, satisfaction):
    global max_satisfaction

    if price > N:
        return
    if idx == M:
        max_satisfaction = max(satisfaction, max_satisfaction)
        return 
    
    dfs(idx + 1, price, satisfaction)
    dfs(idx + 1, price + P[idx], satisfaction + S[idx])

T = int(input())
for tc in range(1, T+1):
    max_satisfaction = 0
    N, M = map(int, input().split())
    P, S = [0] * M, [0] * M
    for i in range(M):
        P[i], S[i] = map(int, input().split())
    dfs(0, 0, 0)

    print(f'#{tc} {max_satisfaction}')