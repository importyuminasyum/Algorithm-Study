answer_set = set(num for num in range(1, 10))

def check_row():
    for row in range(9):
        if set(puzzle[row]) != answer_set:
            return 0
    return 1

def check_col():
    for col in range(9):
        check_set = set()
        for row in range(9):
            check_set.add(puzzle[row][col])
        if check_set != answer_set:
            return 0
    return 1

def check_square():
    for big_row in range(0, 9, 3):
        for big_col in range(0, 9, 3):
            check_set = set()
            for row in range(big_row, big_row + 3):
                for col in range(big_col, big_col + 3):
                    check_set.add(puzzle[row][col])
            if check_set != answer_set:
                    return 0
    return 1

T = int(input())
for tc in range(1, T+1):
    puzzle = [
        list(map(int, input().split()))
        for _ in range(9)
    ]
    print(f'#{tc} {int(check_row() and check_col() and check_square())}')