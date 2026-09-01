pascal = []

for i in range(10):
    row = []

    for j in range(i + 1):
        if j == 0 or j == i:
            row.append(1)
        else:
            row.append(pascal[i-1][j-1] + pascal[i-1][j])
    pascal.append(row)
    
T = int(input())

for tc in range(1, T+1):
    N = int(input())

    print(f'#{tc}')
    for i in range(N):
        print(*pascal[i])