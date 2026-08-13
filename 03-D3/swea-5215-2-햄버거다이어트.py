T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    candidate = {}
    for i in range(1, N+1):
        k, v = map(int, input().split())
        candidate[k] = v # k: 맛, v: 칼로리

    dp = [0] * (L + 1) # 현재까지 칼로리(인덱스)에 대해서 이 칼로리 이하일 때 최대 선호도
    for taste, calorie in candidate.get():
        for c in range(L, calorie - 1, -1):
            dp[c] = max(dp[c], dp[c - calorie] + taste)
        
    print(f'#{tc} {dp[L]}')

    