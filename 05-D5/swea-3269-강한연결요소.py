
def dfs(depth, start_node, cur_node, scc):
    global count

    if depth and cur_node == start_node:
        if scc and scc not in sccs:
            sccs.append(scc)
        return

    for next_node in adj_list[cur_node]:
        scc.append(next_node)
        dfs(depth + 1, start_node, next_node, sorted(scc))
        scc.pop()

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
    sccs = []

    for nodes in adj_list:
        if len(nodes) == 1:
            sccs.append(nodes)

    for start_node in range(1, V + 1):
        dfs(0, start_node, start_node, [])

    sccs = list(map(list, set(map(tuple, sccs))))
    print(sccs)
    print(f'#{tc} {len(sccs)}')