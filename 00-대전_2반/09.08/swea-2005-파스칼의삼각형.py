pascal = [[1], ]
for i in range(1, 11):
    pascal_row = []
    pascal_row.append(1)
    for j in range(1, i):
        pascal_row.append(pascal[i - 1][j] + pascal[i - 1][j - 1])
    pascal_row.append(1)
    pascal.append(pascal_row)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc}')
    for row in range(N):
        print(*pascal[row])
    