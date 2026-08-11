def dfs(idx, A_sum):
    global count

    if A_sum == K:
        count += 1
        return

    if idx >= N:
        return

    dfs(idx+1, A_sum)
    dfs(idx+1, A_sum + A[idx])

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    count, A_sum = 0, 0

    dfs(0, 0)
    print(f'#{tc} {count}')
    