from collections import deque

def bfs(V):
    global result

    que.append(V)
    visited[V] = 1

    while que:
        cur_node = que.popleft()

        for next_node in adj_list[cur_node]:
            if not visited[next_node]:
                visited[next_node] = 1
                que.append(next_node)
                result += 1
    
n = int(input())
m = int(input())

result = 0
visited = [0] * (n + 1)
que = deque()

adj_list = [
    [] for _ in range(n + 1)
]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

bfs(1)

print(result)