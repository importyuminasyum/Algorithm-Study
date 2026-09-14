dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(depth, core, length):
    global max_core, min_length

    if depth == len(core_rcs):
        if core > max_core:
            max_core = core
            min_length = length

        elif core == max_core:
            min_length = min(min_length, length)

        return

    dfs(depth + 1, core, length)

    cr, cc = core_rcs[depth]

    for dr, dc in dirs:
        nr, nc = cr + dr, cc + dc
        path = []

        while in_range(nr, nc):
            
            if maxynos[nr][nc] == '1':
                break

            path.append((nr,nc))

            nr += dr
            nc += dc

        if in_range(nr, nc):
            continue

        for r, c in path:
            maxynos[r][c] = '1'

        dfs(depth + 1, core + 1, length + len(path))

        for r, c in path:
            maxynos[r][c] = '0'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxynos = [list(input().split()) for _ in range(N)]
    min_length = float('inf')
    max_core = 0
    core_rcs = []

    for r in range(1, N-1):
        for c in range(1, N-1):
            if maxynos[r][c] == '1':
                core_rcs.append((r, c))

    dfs(0, 0, 0)

    print(f'#{tc} {min_length}')

    '''
    1. 뭘 선택
    코어와 어느 쪽 벽을 서로 연결할 건지, 연결하지 않을 건지 선택
    가능한 모든 벽 설치
    2. 제약
    벽과 붙어있는 코어는 연결되어 있는 것으로 침
    전선이 교차해서는 안 됨, 원본 배열 수정 필요함
    3. 선택해서 바뀌는 것
    depth, 현재 코어 수, 전선 길이
    4. 뭐가 최대 /  최소
    연결한 코어의 수가 최대일 때, 최소 전선 길이
    '''