T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [
        input()
        for _ in range(N)
    ]
    transpose_board = list(map(list, zip(*board)))

    print(f'#{tc}', end=' ')
    for row in range(N):
        for col in range(N - M + 1):
            palindrome = board[row][col: col + M]
            if palindrome == palindrome[::-1]:
                print(palindrome)
                break

            palindrome2 = transpose_board[row][col:col + M]
            if palindrome2 == palindrome2[::-1]:
                print(''.join(map(str, palindrome2)))
                break
            