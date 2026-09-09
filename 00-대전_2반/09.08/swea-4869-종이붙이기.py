T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dp = [0] * (N // 10 + 1)
    dp[0] = 1

    if N >= 10:
        dp[1] = 1

    for i in range(2, N // 10 + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]

    print(f'#{tc} {dp[N // 10]}')