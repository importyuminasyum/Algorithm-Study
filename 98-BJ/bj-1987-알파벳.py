dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < R and 0 <= c < C

def dfs(depth, r, c):
    global max_move

    max_move = max(depth, max_move)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if in_range(nr, nc) and board[nr][nc] not in check_set:
            check_set.add(board[nr][nc])
            dfs(depth + 1, nr, nc)
            check_set.remove(board[nr][nc])


R, C = map(int, input().split())

board = [
    list(input())
    for _ in range(R)
]

max_move = 0
check_set = {board[0][0]}

dfs(1, 0, 0)

print(max_move)