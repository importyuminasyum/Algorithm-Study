def check(check_arr):
    return len(set(check_arr)) == 9
    
def square_check(square, i, j):
    check_arr = []
    for c in range(i + 3):
        for r in range(j + 3):
            check_arr.append(square[c][r])
    return check(check_arr)

def sudoku_check(arr):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not square_check(arr, i, j):
                return False

    for i in range(9):
        if not check(arr[i]):
            return False

    for i in range(9):
        col = []
        # 81번의 대입 연산
        # copy_arr = list(zip(*arr))
        for j in range(9):
            col.append(arr[j][i])
        if not check(col):
        # if not check(copy_arr[i]):
            return False
    return True

T = int(input())
for test_case in range(1, T + 1):
    arr = [
        list(map(int, input().split())) for _ in range(9)
    ]
    print(f'#{test_case} {int(sudoku_check(arr))}')


# 테케 별 검사 필요
# 1. 행 검사

# 2. 열 검사

# 3. 박스 검사

# 4. 모두 통과하여야 1을 뱉어준다. 단, 1~3 중 불량이 나오면 바로 0