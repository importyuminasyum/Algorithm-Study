import copy
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상

def in_range(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def dfs(depth, copy_bricks):
    '''
    dfs( )
    if 뎁스가 n+1이면 (n번 뽑으면) 
    가지고 있는 벽돌 좌표 돌면서 남은 벽돌 개수 세기
    남은 벽돌 값 반환
    '''
    if depth == N:
        remaining_bricks = 0
        for row_bricks in copy_bricks:
            remaining_bricks += W - row_bricks.count(0)
        return remaining_bricks

    '''
    구슬 폭발 지점 정하기
    열 우선 순회 하면서 0이 아닌 값의 행과 열 가지고 
    0이 아니면
    after boom = 폭발 (폭발지점 폭발 범위 )
    dfs 그 처음 인덱스 depth+1 after boom
    continue
    '''
    min_remaining_bricks = float('inf')
    exploded = False

    for col in range(W):
        for row in range(H):
            if copy_bricks[row][col]: 
                exploded = True
                next_bricks = copy.deepcopy(copy_bricks)
                after_explosion = explosion((row, col, copy_bricks[row][col]), next_bricks)
                min_remaining_bricks = min(min_remaining_bricks, dfs(depth + 1, after_explosion))
                break

    if not exploded:
        return 0

    return min_remaining_bricks

def explosion(exp_info, copy_bricks):
    '''
    폭발:
   구슬 폭발 지점, 폭발 범위 인자로 받기 - 처음에는 정해져있음
   배열 초기화 
   그거 배열에 넣기
    '''
    que = deque()
    que.append(exp_info)
    
    '''
   while 폭발(폭발지점 배열):
   폭발 지점 좌표, 폭발 범위 pop
   
   1. 첫 폭발 지점 폭발 (뭐든지 4방향)
   2. 주변 퍼지기
   0 아닐 때만 
    터뜨리기 가능 - 0으로 수정
    퍼진 애들 좌표랑 값 (0이아닌애들 밀면서) 배열에 넣기
 
    폭발이 끝난 다음에 0 아닌 애들 내리기(3방향)
    바뀐 copy bricks 값 반환
    '''
    while que:
        spread_r, spread_c, spread_range = que.popleft()

        copy_bricks[spread_r][spread_c] = 0

        for dir in range(4):
            for spread in range(1, spread_range):
                nr, nc = spread_r + dirs[dir][0] * spread, spread_c + dirs[dir][1] * spread

                if not in_range(nr, nc, H, W):
                    break
                
                if not copy_bricks[nr][nc]:
                    continue

                if copy_bricks[nr][nc] > 1:
                    que.append((nr, nc, copy_bricks[nr][nc])) # 추가 폭발

                copy_bricks[nr][nc] = 0
                    

    get_off(copy_bricks)

    return copy_bricks

def get_off(copy_bricks):
    for col in range(W):
        bottom = H - 1
        for row in range(H - 1, -1, -1): # 내가 지금 보는 행
            if copy_bricks[row][col]:
                copy_bricks[bottom][col] = copy_bricks[row][col]

                if bottom != row:
                    copy_bricks[row][col] = 0

                bottom -= 1

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [
        list(map(int, input().split()))
        for _ in range(H)
    ]

    remaining_bricks = dfs(0, bricks)
    
    print(f'#{tc} {remaining_bricks}')
    