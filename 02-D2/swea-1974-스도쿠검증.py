# 입력 9 * 9 배열
# 가능 불가능 출력
def can_row():
    for row in range(9):
        if len(set(arr[i])) != 9:
            return 0
    return 1

def can_col():
    for col in range(9):
        col_set = set()

        for row in range(9):
            col_set.add(arr[row][col])

        if len(col_set) != 9:
            return 0
    return 1
        
def can_square():
    for row in range(0, 7, 3):
        for col in range(0, 7, 3):
            square_set = set()
            
            for small_row in range(3):
                for small_col in range(3):
                    square_set.add(arr[row + small_row][col + small_col])

            if len(square_set) != 9:
                        return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    arr = []

    for i in range(9):
        arr.append(list(map(int, input().split())))

    print(f'#{tc} {arr}')
    print(f'#{tc} {int(can_row() and can_col() and can_square())}')