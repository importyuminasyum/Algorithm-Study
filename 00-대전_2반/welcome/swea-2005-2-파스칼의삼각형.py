T = int(input())
for tc in range(1, T+1):
    N = int(input())
    result = []
    
    for i in range(N):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(result[i-1][j-1] + result[i-1][j])
        result.append(row)

    print(f'#{tc}')
    for i in range(N):
        print(*result[i])