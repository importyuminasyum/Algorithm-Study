T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    blocks = sorted(list(map(int, input().split())), reverse=True)
    result = 0

    idx_list = []
    for i in range(1, A + 1):
        idx_list.append(i)
    for i in range(1, B + 1):
        idx_list.append(i)

    idx_list.sort()
    
    for i in range(N):
        result += idx_list[i] * blocks[i]
            
    print(f'#{tc} {result}')