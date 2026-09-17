def inorder(parent):
    global result
    if parent * 2 > N:
        result += tree[parent]
        return

    left = parent * 2
    inorder(left)
    result += tree[parent]
    
    if parent * 2 + 1 <= N:
        right = parent * 2 + 1
        inorder(right)

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N):
        info = list(input().split())
        idx = int(info[0])
        tree[idx] = info[1]

    result = ''
    inorder(1)

    print(f'#{tc} {result}')