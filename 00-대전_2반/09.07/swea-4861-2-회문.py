for tc in range(1, 11):
    N = int(input())
    board = [
        input()
        for _ in range(8)
    ]
    transpose_board = list(map(list, zip(*board)))
    count = 0

    for row in range(8):
        for col in range(9 - N):
            palindrome = board[row][col: col + N]
            if palindrome == palindrome[::-1]:
                count += 1

            palindrome2 = transpose_board[row][col:col + N]
            if palindrome2 == palindrome2[::-1]:
                count += 1
                
    print(f'#{tc} {count}')