W, H = map(int, input().split())
copy_bricks = [
    list(map(int, input().split()))
    for _ in range(W)
]
def in_range(r, c, W, H):
    return 0 <= r < W and 0 <= c < H

for col in range(H):
    bottom = W - 1
    for row in range(W - 1, -1, -1): # 내가 지금 보는 행
        if copy_bricks[row][col]:
            copy_bricks[bottom][col] = copy_bricks[row][col]

            if bottom != row:
                copy_bricks[row][col] = 0

            bottom -= 1
        
print(copy_bricks)

'''

한번이라도 0이 나오면
위에 있는 거 다 한 번씩 아래로 밀기
0 - 한 칸 씩 아래로 밀기
1 - 넘어가기
0 - 한 칸 씩 아래로 밀기
0 - 한 칸 씩 아래로 밀기


'''