def cal_row_count(row):
    result = 0
    count = 0
    for col in range(N):
        if puzzle[row][col]:
            count += 1
        else:
            if count == K:
                result += 1
            count = 0
    if count == K:
        result += 1
    return result

def cal_col_count(col):
    result = 0
    count = 0
    for row in range(N):
        if puzzle[row][col]:
            count += 1
        else:
            if count == K:
                result += 1
            count = 0
    if count == K:
        result += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    result = 0

    puzzle = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    for row in range(N):
        result += cal_row_count(row)

    for col in range(N):
        result += cal_col_count(col)

    print(f'#{tc} {result}')