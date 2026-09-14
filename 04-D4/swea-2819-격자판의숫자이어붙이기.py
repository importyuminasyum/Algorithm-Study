dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < 4 and 0 <= c < 4

def dfs(depth, word, r, c):
    if depth == 6:
        seven_words.add(word)
        return
    
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if not in_range(nr, nc):
            continue

        dfs(depth + 1, word + grid[nr][nc], nr, nc)


T = int(input())
for tc in range(1, T+1):
    grid = [list(input().split()) for _ in range(4)]
    seven_words = set()

    for r in range(4):
        for c in range(4):
            dfs(0, grid[r][c], r, c)

    print(f'#{tc} {len(seven_words)}')
