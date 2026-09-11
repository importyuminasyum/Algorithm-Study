
W, H = map(int, input().split())
cur_bricks = [
    list(map(int, input().split()))
    for _ in range(H)
]

for col in range(H):
    bottom = W - 1
    for row in range(W -1, -1, -1):
        if cur_bricks[bottom][col]:
            bottom -= 1 
            continue
            
        if cur_bricks[row][col]:
            cur_bricks[bottom][col], cur_bricks[row][col] = cur_bricks[row][col], cur_bricks[bottom][col]
            
print(cur_bricks)