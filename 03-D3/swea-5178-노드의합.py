def calc_tree():
    for parent in range(N // 2, 0, -1):
        left = parent * 2
        right = parent * 2 + 1

        tree[parent] = tree[left]

        if right <= N:
            tree[parent] += tree[right]

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        leaf_idx, num = map(int, input().split())
        tree[leaf_idx] = num
        
    calc_tree()

    print(f'#{tc} {tree[L]}')