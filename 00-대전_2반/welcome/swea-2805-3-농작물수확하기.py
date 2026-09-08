T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = []
    count = 0

    for i in range(N):
        field.append(list(map(int, input())))

    mid = N // 2
    for i in range(N):
        blue = abs(mid - i)
        count += sum(field[i][blue:N - blue])

    print(f'#{tc} {count}')