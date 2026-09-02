def cal_row_max():
    row_max = float('-inf')
    for row in range(100):
        row_sum = sum(arr[row])
        row_max = max(row_max, row_sum)

    return row_max

def cal_col_max():
    col_max = float('-inf')
    for col in range(100):
        col_sum = 0
        for row in range(100):
            col_sum += arr[row][col]
        col_max = max(col_max, col_sum)
    
    return col_max

def cal_diagonal_max():
    diagonal_sum1, diagonal_sum2 = 0, 0
    for diagonal in range(100):
        diagonal_sum1 += arr[diagonal][diagonal]
        diagonal_sum2 += arr[99 - diagonal][diagonal]
    
    return max(diagonal_sum1, diagonal_sum2)

for _ in range(10):
    t = int(input())
    arr = [
        list(map(int, input().split()))
        for _ in range(100)
    ]
    
    print(f'#{t} {max(cal_row_max(), cal_col_max(), cal_diagonal_max())}')