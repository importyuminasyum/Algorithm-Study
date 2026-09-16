from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visited[start] = 1

    while que:
        cur_node = que.popleft()

        for next_node in adj_list[cur_node]:
            if visited[next_node]:
                continue

            que.append(next_node)
            visited[next_node] = visited[cur_node] + 1

    count = 0

    for x in visited:
        if 1 < x <= 3:
            count += 1

    return count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    print(f'#{tc} {bfs(1)}')