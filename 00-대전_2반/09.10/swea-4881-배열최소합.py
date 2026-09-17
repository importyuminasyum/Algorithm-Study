def cal_min_sum(r, cur_sum):
    global result

    if cur_sum >= result:
        return

    if r == N:
        result = min(cur_sum, result)
        return
    
    for c in range(N):
        if visited[c]:
            continue

        visited[c] = 1
        cal_min_sum(r + 1, cur_sum + arr[r][c])
        visited[c] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N # 고른 열
    result = float('inf')
    cal_min_sum(0, 0)
    print(f'#{tc} {result}')