def dfs(cur_node):
    global result
    visited[cur_node] = 1

    for next_node in adj_list[cur_node]:
        if visited[next_node]:
            continue

        visited[next_node] = 1
        result += 1
        dfs(next_node)

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    adj_list = [[] for _ in range(E + 2)]
    visited = [0] * (E + 2)
    result = 1
    for i in range(0, E * 2, 2):
        adj_list[nodes[i]].append(nodes[i + 1])

    dfs(N)
    print(f'#{tc} {result}')