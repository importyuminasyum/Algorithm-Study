T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    gonfalon = [list(input()) for _ in range(N)]
    min_coloring_count = float('inf')
    count_value = {'W': [], 'B': [], 'R': []}

    for r in range(N):
        count_value['W'].append(M - gonfalon[r].count('W'))
        count_value['B'].append(M - gonfalon[r].count('B'))
        count_value['R'].append(M - gonfalon[r].count('R'))

    for top in range(N - 2):
        for bottom in range(top + 1, N - 1):
            top_w = (0, top)
            middle_b = (top + 1, bottom)
            bottom_r = (bottom + 1, N - 1)

            count = sum(count_value['W'][:top + 1]) + sum(count_value['B'][top + 1:bottom + 1]) + sum(count_value['R'][bottom + 1:N])
            min_coloring_count = min(count, min_coloring_count)

    print(f'#{tc} {min_coloring_count}')