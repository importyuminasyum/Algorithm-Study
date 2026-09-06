def perm(depth, cur_length):
    global min_length
    if depth == N:
        min_length = min(cur_length, min_length)
        return

    for i in range(N):
        

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rcs = list(map(int, input().split()))
    company = tuple(rcs[0:2])
    home = tuple(rcs[2:4])

    customers = []
    for i in range(4, 2 * N + 4 , 2):
        customers.append(tuple(rcs[i:i + 2]))

    min_length = float('inf')

    perm(1, 0)

    print(f'#{tc} {min_length}')
