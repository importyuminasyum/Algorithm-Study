from collections import deque

def dfs(dfs_graph, visited, V):
    result = []
    # 스택 
    stack = deque([V])

    # 반복 (언제까지? 모두 방문할 때까지 - stack이 비기 전까지)
    while stack:
        # 2. 스택에서 pop 후 저장
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = 1
        result.append(node)

        # 4. 대상노드 자식 노드가 방문한 적이 없다면 스택에 추가
        for i in range(len(dfs_graph) - 1, 0, -1):
            if dfs_graph[node][i]:
                stack.append(i)

    return result

def dfs_recursive(dfsr_graph, visited, V):
    result = []
    # 재귀
    # 1. 대상 노드 방문 체크
    visited[V] = 1
    # 2. 대상 노드 출력
    result.append(V)

    # 3. 그 대상 노드 인덱스 값이 1인 인덱스에 대해서, 그리고 방문하지 않았다면 DFSR(자식노드) 시행
    for i in range(1, len(dfsr_graph)):
        if dfsr_graph[V][i] and not visited[i]:
            result.extend(dfs_recursive(dfsr_graph, visited, i))

    return result

def bfs(bfs_graph, visited, V):
    result = []
    # 큐
    queue = deque()
    # 1. 초기값 큐에 넣기
    queue.append(V)
    visited[V] = 1
    # 반복 (언제까지? 모두 방문할 때까지 - 큐가 비기 전까지)
    while queue:
        # 2. 큐에서 popleft 후 저장
        node = queue.popleft()
        result.append(node)

        # 4. 대상 노드 자식 노드가 방문한 적이 없다면 큐에 추가
        for i in range(1, len(bfs_graph)):
            if bfs_graph[node][i] and not visited[i]:
                visited[i] = 1
                queue.append(i)

    return result

N, M, V = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]

# 안접 행렬 만들기 - 인덱스가 곧 노드
for i in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

print(*dfs(matrix, [0] * (N + 1), V))
print()
print(*dfs_recursive(matrix, [0] * (N + 1), V))
print()
print(*bfs(matrix, [0] * (N + 1), V))