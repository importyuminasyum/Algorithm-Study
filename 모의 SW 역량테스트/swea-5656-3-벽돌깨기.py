'''
구슬: N번 쏠 수 있음
벽돌 정보: H * W 배열

H: 행, W: 열
행 우선 순회 시:
for row in range(H):
    for col in range(W):
    
열 우선 순회 시
for col in range(W):
    for row in range(H):
    
구슬은 좌, 우로만 이동 가능 - 맨 위에 있는 벽돌만
숫자 1~9로 표현
구슬 명중하면 상하좌우로 그 벽돌의 숫자 - 1칸 만큼 동시 폭발
1. 구슬이 열 탐색하다가 한 지점에 떨어짐
2. 가장 위 열의 벽돌이 터지기 시작, 
3. 그 벽돌의 숫자 -1 칸 만큼 폭발이 퍼지기 - 0으로 바뀜
4. 영향을 받은 벽돌의 숫자 -1 칸 만큼 폭발이 퍼지기
5. 폭발이 모두 끝난 후에 중력 작동
다시 1로..

가장 많은 벽돌을 제거한 경우에 대해서 남은 벽돌 개수 구하기 - 마지막에 가장 적게 남은 벽돌 수 구하기
'''

'''

처음 한 벽돌 선택 / 폭발 / 연쇄 폭발 / 중력 작용
/ 다음 벽돌 선택 / 폭발 / 연쇄 폭발 / 중력 작용
...
언제까지? N번 구슬을 사용했을 때까지
dfs(0, bricks) - 0개의 구슬을 처리한 상태

구조
dfs(depth, cur_bricks)
- 정의: depth개의 구슬을 처리한 상태
- 인자: depth, depth - 1개의 구슬을 처리한 후 벽돌 정보
- return: N개의 depth를 처리한 이후의 벽돌 상태에 대해 남은 벽돌 수들의 최솟값
종료조건: depth가 N이 되었을 때
    remaining_bricks = 0

    for row in range(H):
        remaining_bricks += W - cur_bricks[row].count(0)
    min_remaining_bricks = min(remaining_bricks, min_remaining_bricks)

    return min_remaining_bricks

구슬을 떨어뜨릴 벽돌 선택 - 열 우선 순회 / 0이 아닌 벽돌 찾으면 폭발하고 다음 열로
폭발 작용

for col in range(W):
    for row in range(H):
        if cur_bricks[row][col]:
            변경할 벽돌 정보 copy
            next_bricks = copy.deepcopy(cur_bricks)
            지금 떨어뜨린 구슬로 폭발 처리
            dfs(depth + 1, implementation((row, col, next_bricks[row][col]), next_bricks))
            break
'''

'''
implementation(exploded_info(행, 열, 범위), cur_bricks):
- 정의: 폭발이 시작되는 지점과 폭발 범위를 받아 현재 벽돌 정보 처리
1. 첫번째 폭발 당시 벽돌 정보 처리
2. 연쇄 폭발 시 벽돌 정보 처리
3. 모든 폭발이 끝난 후 중력 작용 함수 적용
- 인자: 폭발 지점, 범위, 처리할 벽돌 정보
- return: 처리가 끝난 벽돌 정보

bfs로 구현 - que에 넣기

cur_bricks[exploded_row][exploded_col] = 0

que = deque()
que.append(exploded_info)

1. 첫번째 폭발 당시 벽돌 정보 처리
while que:
    exploded_row, exploded_col, exploded_range = que.pop()
    cur_bricks[exploded_row][exploded_col] = 0 
    4방향 폭발 처리하면서 연쇄 폭발할 벽돌 que에 담기
    for dr, dc in dirs:
        for spread in range(1, exploded_range):
            nr, nc = exploded_row + dr * spread, exploded_col + dc * spread

            if not in_range(nr, nc, H, W):
                break
                
            if not cur_bricks[nr][nc]:
                continue
            
            # 폭발 처리
            cur_bricks[nr][nc] = 0
            if cur_bricks[nr][nc] > 1:
                que.append((nr, nc, cur_bricks[nr][nc]))
    
# 중력 작용 함수
get_off(cur_bricks)
return cur_bricks
            
'''

'''
get_off(cur_bricks):
- 받은 bricks 정보에 대해서 각 열에 대해 0 위에 0 이상의 수가 있다면 그 수 만큼 내리기
- 인자: bricks 정보


열 우선 순회
한 열에 대해서
1 1 1
0 0 0
0 0 0
행 기준 역방향, 0인 한 지점에 대해서 
그 위를 순회하다가 0이 아닌 지점을 발견하면 자리 바꾸기

for col in range(H):
    bottom = W - 1
    for row in range(W -1, -1, -1):
        if cur_bricks[bottom][col]:
            bottom -= 1 
            continue
            
        if cur_bricks[row][col]:
            cur_bricks[bottom][col], cur_bricks[row][col] = cur_bricks[row][col], cur_bricks[bottom][col]
'''
import copy
from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, H, W):
    return 0 <= r < H and 0 <= c < W

def dfs(depth, cur_bricks):
    '''
    - 정의: depth개의 구슬을 처리한 상태
    - 인자: depth, depth - 1개의 구슬을 처리한 후 벽돌 정보
    - return: N개의 depth를 처리한 이후의 벽돌 상태에 대해 남은 벽돌 수들의 최솟값
    종료조건: depth가 N이 되었을 때
    '''
    global min_remaining_bricks

    if depth == N:
        remaining_bricks = 0

        for row in range(H):
            remaining_bricks += W - cur_bricks[row].count(0)
            
        min_remaining_bricks = min(remaining_bricks, min_remaining_bricks)

        return
    
    # 구슬을 떨어뜨릴 벽돌 선택 - 열 우선 순회 / 벽돌 찾으면 폭발하고 다음 열로
    # 플래그 설정해서 만약 벽돌이 하나도 없을 때는 0 반환
    exploded = False

    for col in range(W):
        for row in range(H):
            if cur_bricks[row][col]:
                exploded = True
                # 변경할 벽돌 정보 copy
                next_bricks = copy.deepcopy(cur_bricks)
                # 지금 떨어뜨린 구슬로 폭발 처리
                dfs(depth + 1, implementation((row, col, next_bricks[row][col]), next_bricks))
                break

    if not exploded:
        min_remaining_bricks = 0
        return


def implementation(exploded_info, next_bricks):
    '''
    - 정의: 폭발이 시작되는 지점과 폭발 범위를 받아 현재 벽돌 정보 처리
    1. 첫번째 폭발 당시 벽돌 정보 처리
    2. 연쇄 폭발 시 벽돌 정보 처리
    3. 모든 폭발이 끝난 후 중력 작용 함수 적용
    - 인자: 폭발 지점, 범위, 처리할 벽돌 정보
    - return: 처리가 끝난 벽돌 정보
    '''

    # bfs로 구현 - que에 넣기
    que = deque()
    que.append(exploded_info)

    # 1. 첫번째 폭발 당시 벽돌 정보 처리
    while que:
        exploded_row, exploded_col, exploded_range = que.popleft()
        next_bricks[exploded_row][exploded_col] = 0 

        # 4방향 폭발 처리하면서 연쇄 폭발할 벽돌 que에 담기
        for dr, dc in dirs:
            for spread in range(1, exploded_range):
                nr, nc = exploded_row + dr * spread, exploded_col + dc * spread

                if not in_range(nr, nc, H, W):
                    break

                value = next_bricks[nr][nc]

                if not value:
                    continue
                
                # 폭발 처리
                if value > 1:
                    que.append((nr, nc, next_bricks[nr][nc]))

                next_bricks[nr][nc] = 0
        
    # 중력 작용 후 return
    return get_off(next_bricks)

def get_off(next_bricks):
    '''
    - 받은 bricks 정보에 대해서 각 열에 대해 0 위에 0 이상의 수가 있다면 그 수 만큼 내리기
    - 인자: bricks 정보
    - return: 변경한 bricks

    열 우선 순회
    한 열에 대해서
    1 1 1
    0 0 0
    0 0 0
    행 기준 역방향, 0인 한 지점에 대해서 
    그 위를 순회하다가 0이 아닌 지점을 발견하면 자리 바꾸기
    '''

    for col in range(W):
        bottom = H - 1
        for row in range(H -1, -1, -1):
            if next_bricks[row][col]:
                next_bricks[bottom][col], next_bricks[row][col] = next_bricks[row][col], next_bricks[bottom][col]
                bottom -= 1

    return next_bricks

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [
        list(map(int, input().split()))
        for _ in range(H)
    ]

    min_remaining_bricks = float('inf')

    dfs(0, bricks)

    print(f'#{tc} {min_remaining_bricks}')