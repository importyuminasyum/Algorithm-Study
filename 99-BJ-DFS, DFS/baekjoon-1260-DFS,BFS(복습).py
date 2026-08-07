from collections import defaultdict, deque

def dfs(V):
    stack = deque()
    stack.append(V)

    while stack:
        cur_node = stack.pop()

        if visited[cur_node]:
            continue

        visited[cur_node] = 1
        print(cur_node, end = ' ')

        for next_node in reversed(adj_list[cur_node]):
            if not visited[next_node]:
                stack.append(next_node)

def dfs_rec(cur_node):
    visited[cur_node] = 1
    print(cur_node, end = ' ')

    for next_node in adj_list[cur_node]:
        if visited[next_node]:
            continue

        dfs_rec(next_node)

def bfs(V):
    queue = deque()

    queue.append(V)
    visited[V] = 1

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end = ' ')
        
        for next_node in adj_list[cur_node]:
            if visited[next_node]:
                continue

            queue.append(next_node)
            visited[next_node] = 1

N, M, V = map(int, input().split())

adj_list = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
    adj_list[i].sort()

visited= [0] * (N + 1)

dfs(V)
print()

stack = deque()
visited= [0] * (N + 1)

dfs_rec(V)
print()

visited= [0] * (N + 1)
bfs(V)