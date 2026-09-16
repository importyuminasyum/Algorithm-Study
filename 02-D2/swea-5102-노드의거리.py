from collections import deque

def bfs(S, G):
    que = deque()
    que.append(S)
    visited[S] = 1
    count = 0

    while que:
        cur_node = que.popleft()
        for next_node in adj_list[cur_node]:
            if visited[next_node]:
                continue

            if next_node == G:
                return visited[cur_node]

            que.append(next_node)
            visited[next_node] = visited[cur_node] + 1

    return 0

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)
    S, G = map(int, input().split())
    visited = [0] * (V + 1)
    print(f'#{tc} {bfs(S, G)}')
