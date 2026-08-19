def dfs(N):
    global answer

    answer += 1

    for i in range(0, len(tree), 2):
        if tree[i] == N:
            dfs(tree[i + 1])
    
T = int(input())
for tc in range(1, T+1):
    answer = 0
    E, N = map(int, input().split())
    tree = list(map(int, input.split()))
    dfs(N)
    
    print(f'{tc} {answer}')