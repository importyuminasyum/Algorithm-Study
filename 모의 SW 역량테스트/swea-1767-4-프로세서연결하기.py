'''
maxynos = 가로 N / 세로 N의 cell
core와 가장자리를 연결하는 전선 설치 - 직선만 가능, 서로 교차는 불가
가장자리는 이미 전원이 연결됨

최대한 많은 core에 전원을 연결하였을 경우, 전선 길이의 합
여러 방법이 있을 경우, 전선 길이의 합이 최소가 되는 값

최대한 많은 core에 전원을 연결해도, 전원이 연결되지 않는 core 존재할 수 있음

일단 core_rcs 부터 확인 / 탐색 - 가장자리 제외 / n-1,n-1만 탐색
dfs - core 하나씩 연결해보고 내려가기
방문 배열 필요함
한 core가 연결 할 수 있는 가지 - 최소 0개, 최대 4개
연결했다면? 그 상태를 0로 변경
지금까지 연결한 core수, 같다면 그때의 전선 길이 최소여야 함
같이 가지고 있어야 함

모든 core_rcs 돌면서 - 곧 depth
maxynos 변경
core 수, 그때의 전선 길이 같이 가지고 가기

depth가 core_rcs일때, 
현재 도착한 core 수가 최댓값보다 적다면 더 안 봄
같다면, 전선 길이 최솟값을 비교 갱신


어떻게 들어가?
이거 순열이지...
5개 중에 줄 세우는 경우의 수 만큼 탐색해야 함
탐색 어떻게?

한 core_rc 좌표부터 시작
4방향에 대해서 순회
한 방향이
- 전선 연결 가능?
- 다음 core_rc 좌표 선택

- 전선 연결 불가능?
- 그래도 다음 core_rc 좌표 선택


'''
'''
dfs(depth, cur_maxynos, cul_core, cul_length):

if depth == len(core_rcs):
    if cul_core > max_core:
        return

    max_core = max(cul_core, max_core)
    
    elif cul_core == max_core:
        min_length = min(cul_length, min_length)
    
    visited = [0] * len(core_rcs)

    return
    
for V in range(len(core_rcs)):
    방문 처리 - 방문한 적 있으면 continue
    if visited[V]:
        continue
        
    visited[V] = 1
    core_r, core_c = core_rcs[V][0], core_rcs[V][1]

    for dr, dc in dirs:
        전선 연결 가능 여부 판단 / 길이 반환 함수
        length = check_link(core_r, core_c, dr, dc)
        if length:
            next_maxynos = copy.deepcopy(next_maxynos)
            maxynos 상태 변경 함수
            for cable in range(1, length + 1):
                    nr, nc = core_r * cable, core_c * cable
                    next_maxynos[nr][nc] = 1
            
            dfs(다음 좌표 선택) - next 변경한 maxynos
            dfs(depth + 1, next_maxynos, core + 1, cul_legnth + length)
        else:
            dfs(다음 좌표 선택)
            dfs(depth + 1, cur_maxynos, core, cul_legnth)

  
def check_link(core_r, core_c, dr, dc):
    # 다음 좌표 지정
    nr, nc = core_r + dr, core_c, dc
    length = 0

    while not in_range(nr, nc):
        length += 1

        if maxynos[nr][nc]:
            return 0

        nr, nc = nr + dr, nr + dc
        
    else:
        return length

    return 0

'''

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def dfs(depth, cul_core, cul_length):
    global max_core, min_length

    if depth == len(core_rcs):
        if cul_core > max_core:
            max_core = cul_core
            min_length = cul_length

        elif cul_core == max_core:
            min_length = min(cul_length, min_length)
        
        return
    
    core_r, core_c = core_rcs[depth]
    
    for dr, dc in dirs:
        # 전선 연결 가능 여부 판단 / 길이 반환 함수
        length = check_link(core_r, core_c, dr, dc)

        if length:
            nr, nc = core_r + dr, core_c + dc

            while in_range(nr, nc, N):
                maxynos[nr][nc] = 1
                nr, nc = nr + dr, nc + dc
            
            dfs(depth + 1, cul_core + 1, cul_length + length)

            nr, nc = core_r + dr, core_c + dc
            
            while in_range(nr, nc, N):
                maxynos[nr][nc] = 0
                nr, nc = nr + dr, nc + dc

    dfs(depth + 1, cul_core, cul_length)

  
def check_link(core_r, core_c, dr, dc):
    # 다음 좌표 지정
    nr, nc = core_r + dr, core_c + dc
    length = 0

    while in_range(nr, nc, N):
        length += 1

        if maxynos[nr][nc]:
            return 0

        nr, nc = nr + dr, nc + dc
        
    else:
        return length


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxynos = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    core_rcs = []
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if maxynos[row][col]:
                core_rcs.append((row, col))
    max_core, min_length = 0, float('inf')

    dfs(0, 0, 0)

    print(f'#{tc} {min_length}')