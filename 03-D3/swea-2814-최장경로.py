# N, M: node, edge
# adj_list
# 최장경로 계산
# 재귀로 풀기
def dfs(V, count):
    global max_result
    
    max_result = max(max_result, count)

    for next_node in adj_list[V]:
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, count + 1)
            visited[next_node] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    info = [
        list(map(int, input().split()))
        for _ in range(M)
    ]
    visited = [0] * (N + 1)

    adj_list = [
        [] for _ in range(N + 1)
    ]
    for a, b in info:
        adj_list[a].append(b)
        adj_list[b].append(a)

    max_result = 0

    for start in range(1, N + 1):
        visited[start] = 1
        dfs(start, 1)
        visited[start] = 0

    print(f'#{tc} {max_result}')