T = int(input())
for tc in range(1, T+1):
    N = int(input())
    before_row = []

    print(f'#{tc}')

    for i in range(N):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(before_row[j-1] + before_row[j])

        print(*row)
        before_row = row