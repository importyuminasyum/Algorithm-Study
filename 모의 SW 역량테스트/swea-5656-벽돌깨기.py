'''
입력
N, M, H - 구슬을 쏠 수 있는 횟수, W * H 배열
빈공간 - 0, 벽돌 - 외 숫자

알고리즘
구슬은 좌, 우로만, 항상 맨 위의 벽돌만
구슬이 명중한 벽돌은 (벽돌에 적힌 숫자 - 1)칸 만큼 같이 제거
만약 8에 맞았으면 양 옆 7칸이 동시에 제거됨
제거했을 때 0이 되었으면 그 위에 있던 벽돌이 아래로 떨어짐

N개의 벽돌을 떨어뜨려 최대한 많은 벽돌 제거

출력
남은 벽돌의 개수

1. 구슬을 떨어뜨린다
2. 폭발이 4방향으로 퍼진다
3. 폭발 당한 벽돌 (0이 된)은 그 위 배열을 하나씩 내린다
4. 그 다음 구슬을 떨어뜨린다
...
5. 구슬을 다 떨어뜨린 후 전체 벽돌 개수를 센다


일단 순열 - 구슬을 떨어뜨릴 수 있는 경우의 수: 순서 o, W perm N
max_remaining_bricks = float('-inf')
for perm in permutations(range(W), N) # 구슬 떨어뜨리는 인덱스 경우의 수
그 순열 인덱스 한 쌍에 대해서
    copy_bricks = copy.deepcopy(bricks)
    max_remaining_bricks = max(max_remaining_bricks, one_explosion(perm, copy_bricks))

한 폭발:
    구슬 순회
    - 첫 구슬 떨어지면
    for bead in perm:
        for row in range(H):
            if copy_bricks[row][bead]:
                spread_range = copy_bricks[row][bead]
                row, bead = center_r, center_c
                break
                
        그 때 열 순회하다가 처음으로 0이 아니게 되는 칸의 숫자가 spread_range, 
        그 때 행과 열 좌표가 3방향으로 퍼져나갈 중심점 (center_r, center_c)

        for dr, dc in dirs: # 한 방향 당 spread
            push_rcs = []
            중심점을 기준으로 3방향씩(우, 하, 좌만) 퍼져 나가기,
            for spread in range(1, spread_range):
                nr, nc = center_r + dr * spread, center_c + dc * spread

                if not in_range(nr, nc, W): # 왜? 그 방향으로는 더 못 감
                    break 
                    
                if copy_bricks[nr][nc] > 1:
                    copy_bricks[nr][nc] -= 1

                if copy_bricks[nr][nc] == 1:
                    copy_bricks[nr][nc] = 0
                    push_rcs.append((nr, nc))
                
        그 열의 행을 하나씩 내리기
        get_off(nr, nc)
        for nr, nc in push_rcs:
            for row in range(nr - 1, -1, -1): # row: 내가 확인할 좌표
                if not copy_bricks[row][nc]:
                    break
                
                copy_bricks[row + 1][nc] = copy_bricks[row][nc]
            copy_bricks[0][nc] = 0

    remaing_bricks = 0
    for row in copy_bricks:
        remaing_bricks += sum(row)
      
    return remaing_bricks

구슬 떨어뜨리고
폭발하고
주변 벽돌 내려가고

벽돌 개수 세고

'''
import copy
from itertools import permutations

dirs = [(0, 1), (1, 0), (0, -1)] # 우, 하, 좌

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def one_explosion(perm, copy_bricks):
    for bead in perm:
        
        for row in range(H):
            if copy_bricks[row][bead]:
                spread_range = copy_bricks[row][bead]
                center_r, center_c = row, bead
                break

        for dr, dc in dirs: # 한 방향 당 spread
            push_rcs = []
            for spread in range(1, spread_range):
                nr, nc = center_r + dr * spread, center_c + dc * spread

                if not in_range(nr, nc, W): # 왜? 그 방향으로는 더 못 감
                    break 
                    
                if copy_bricks[nr][nc] > 1:
                    copy_bricks[nr][nc] = 0

                if copy_bricks[nr][nc] == 1:
                    copy_bricks[nr][nc] = 0
                    push_rcs.append((nr, nc))
                
        for nr, nc in push_rcs:
            for row in range(nr - 1, -1, -1): # row: 내가 확인할 좌표
                if not copy_bricks[row][nc]:
                    break
                
                copy_bricks[row + 1][nc] = copy_bricks[row][nc]
            copy_bricks[0][nc] = 0

    remaing_bricks = 0

    for row in range(W):
        for col in range(H):
            if copy_bricks[row][col]:
                remaing_bricks += 1
      
    return remaing_bricks
 
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [
        list(map(int, input().split()))
        for _ in range(W)
    ]
    max_remaining_bricks = float('-inf')

    for perm in permutations(range(W), N): # 구슬 떨어뜨리는 인덱스 경우의 수
        copy_bricks = copy.deepcopy(bricks) 
        max_remaining_bricks = max(max_remaining_bricks, one_explosion(perm, copy_bricks))

    print(f'#{tc} {max_remaining_bricks}')
    