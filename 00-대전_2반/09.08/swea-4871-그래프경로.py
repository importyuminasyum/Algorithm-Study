'''
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''

def dfs(cur_node):
    visited[cur_node] = 1

    for next_node in adj_list[cur_node]:
        if not visited[next_node]:
            dfs(next_node)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)

    S, G = map(int, input().split())
    visited = [0] * (V + 1)

    dfs(S)

    if visited[G]:
        result = 1
    else:
        result = 0

    print(f'#{tc} {result}')
    