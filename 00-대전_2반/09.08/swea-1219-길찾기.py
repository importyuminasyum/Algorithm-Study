def dfs(cur_node):
    visited[cur_node] = 1

    for next_node in adj_list[cur_node]:
        if not visited[next_node]:
            dfs(next_node)

for tc in range(1, 11):
    T, E = map(int, input().split())
    result = 0

    adj_list = [[] for _ in range(100)] 
    roads = list(map(int, input().split()))

    for i in range(0, 2 * E, 2):
        adj_list[roads[i]].append(roads[i + 1])

    visited = [0] * 100
    dfs(0)

    if visited[99]:
        result = 1

    print(f'#{T} {result}')