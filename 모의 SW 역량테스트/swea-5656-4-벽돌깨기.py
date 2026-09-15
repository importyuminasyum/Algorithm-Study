'''
W * H - 열 * 행
H: 행
W: 열

구슬 떨구는 경우: 순열 W개 중 N개 뽑기

1. 구슬이 떨어지면 - 그 열에서 맨 위에 있는 벽돌만 깨짐
2. 벽돌은 숫자로 표현, 구슬에 맞으면 상하좌우로 벽돌에 적힌 수 - 1 칸 만큼 제거
3. 연쇄 폭발

'''
from itertools import product
from collections import deque
import copy

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < H and 0 <= c < W

def explosion(shoot_idx, bricks):
    global burnt_bricks

    # 구슬이 한 개 들어왔을 때 
    que = deque()

    for r in range(H):
        if bricks[r][shoot_idx]:
            # 터트릴 시작 지점 선정
            que.append((r, shoot_idx, bricks[r][shoot_idx]))
            bricks[r][shoot_idx] = 0
            break

    # 구슬이 내려오면서 영향을 주는 칸들 생김
    while que:
        # 폭발이 퍼져나갈 시점 선택
        cr, cc, exp_range = que.popleft()
        burnt_bricks += 1

        for dr, dc in dirs:
            for exp in range(1, exp_range):
                nr, nc = cr + dr * exp, cc + dc * exp

                if not in_range(nr, nc):
                    continue

                if bricks[nr][nc]:
                    que.append((nr, nc, bricks[nr][nc]))
                    bricks[nr][nc] = 0

    # 남은 벽돌들에 대해서 중력 작용
    bricks = gravitational_action(bricks)
    return

def gravitational_action(prev_bricks):
    for c in range(W):
        bottom = H - 1
        for r in range(H - 1, -1, -1):
            if prev_bricks[r][c]:
                prev_bricks[bottom][c], prev_bricks[r][c] = prev_bricks[r][c], prev_bricks[bottom][c]
                bottom -= 1

    return prev_bricks


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks_original = [list(map(int, input().split())) for _ in range(H)]
    max_bricks = 0

    initial_value = 0
    for r in range(H):
        initial_value += W - bricks_original[r].count(0)

    for perm in product(range(W), repeat=N):
        bricks = copy.deepcopy(bricks_original)
        burnt_bricks = 0

        for shoot_idx in perm:
            # 벽돌 폭발 - 연쇄 폭발 - 중력 작용
            # 출력: 터진 벽돌
            explosion(shoot_idx, bricks)

        max_bricks = max(burnt_bricks, max_bricks)
    
    print(f'#{tc} {initial_value - max_bricks}')



