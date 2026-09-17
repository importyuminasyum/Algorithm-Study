def inorder(parent):
    if len(tree[parent]) >= 2:
        left = int(tree[parent][1])
        inorder(left)

    result.append(tree[parent][0])
    
    if len(tree[parent]) == 3:
        right = int(tree[parent][2])
        inorder(right)

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    result = []
    for _ in range(N):
        info = list(input().split())
        idx = int(info[0])
        tree[idx] = info[1:]
    
    inorder(1)

    print(f'#{tc} {"".join(result)}')