from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, visited, node)

def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for node in graph[v]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)


N, M, V = map(int, input().split())

# 인접 리스트
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited = [False] * (N + 1)
dfs(graph, visited, V)

print()

# BFS
visited = [False] * (N + 1)
bfs(graph, visited, V)