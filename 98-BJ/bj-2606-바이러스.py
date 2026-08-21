def dfs(V):
    global result

    visited[V] = 1

    if not adj_list[V]:
        return

    for cur_node in adj_list[V]:
        if not visited[cur_node]:
            result += 1
            dfs(cur_node)
    
n = int(input())
m = int(input())

result = 0
visited = [0] * (n + 1)

adj_list = [
    [] for _ in range(n + 1)
]

for _ in range(m):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs(1)

print(result)