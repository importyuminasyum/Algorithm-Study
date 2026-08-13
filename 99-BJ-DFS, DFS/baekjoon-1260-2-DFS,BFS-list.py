from collections import deque, defaultdict
def dfs(cur_node):
    # 방문체크
    visited[cur_node] = 1
    print(cur_node, end = ' ')

    # 노드 탐색 시작 인접 리스트 순회하면서 방문하지 않은 노드에 대해서 재귀 dfs(그노드)
    for next_node in adj_list[cur_node]:
        if visited[next_node]:
            continue

        dfs(next_node)
    
def bfs(V):
    # 시작노드 큐에 추가 - 방문 체크
    # 이거 반복, 언제까지? 큐 빌 때까지
    # pop 하면서 그 값 저장하고
    # 그 값을 기준으로 방문하지 않은 아래노드 다 큐에 넣기 
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

queue = deque()

for i in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for i in range(1, N + 1):
    adj_list[i].sort()

visited = [0] * (N + 1)
dfs(V)
print()
visited = [0] * (N + 1)
bfs(V)
