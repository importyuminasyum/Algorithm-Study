T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input()))

    max_count, count = 0, 0

    for a in A:
        if a == 1:
            count += 1
            max_count = max(count, max_count)

        else:
            count = 0

    print(f'#{tc} {max_count}')
