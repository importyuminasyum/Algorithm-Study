# 초기 배열 생성해서 입력 받기
# deepcopy해서 한 번 트라이마다 - 모든 노드 다 돌 때마다 사용하고 초기화 할 것
# 결과 담을 count - 한 번 트라이마다 최솟값 갱신
# 1~n-1, 1~n-1 확인한다음 coordinates에 튜플로 x, y 담기
# 출력: 모든 트라이에서 최솟값

# can_connect
# 전선 연결 가능 여부 확인
# 가능하면 그때 연결한 전선 개수 더하기
# 불가능하면 0 반환

# set_wire
# 가능한 방향에 대해서 maxynos 수정 
# 다만 dfs 이후에 다시 초기화 해줘야 함

# dfs(depth, 연결한 코어 수, 전선 길이)
# 종료 조건: depth가 총 코어 수와 같을 때 (coordinate 길이), total_core_count에 max 저장하고, 그 값이 현재 값과 같을 경우에만 total_wire_length min 값 저장
# 현재 코어 하나 선택
# 1. 4방향 각각에 대해서
# - 끝까지 갈 수 있는지 먼저 확인 can_connect
# - 가능하면 전선 설치 ser_wire
# - dfs(다음 코어)
# - 전선 제거

# 2. 이 코어를 연결하지 않는 경우에도 
# - dfs(다음 코어)

# dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
# dir = 0
# x + dirs[dir], y + dirs[dir] 

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우하좌상

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

def can_connect(dir, x, y): # 현재 좌표에서 dir 방향으로 끝까지 갈 수 있는지 없는지 판단
    length = 0
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]

    # 현재 방향으로 끝까지 가면서 한 번이라도 1 만나면 False, 아니면 True
    while in_range(nx, ny, N):
        if maxynos[nx][ny]:
            return 0
        
        length += 1
        nx, ny = nx + dirs[dir][0], ny + dirs[dir][1]
        
    return length

def set_wire(dir, x, y, value):
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]

    while in_range(nx, ny, N):
        maxynos[nx][ny] = value
        nx, ny = nx + dirs[dir][0], ny + dirs[dir][1]

def dfs(depth, core_count, wire_length):
    global max_core_count, min_wire_length

    total_core_count = len(coordinates) # 전체 코어 개수 (가장자리 제외)

    if depth == total_core_count:
        if core_count > max_core_count:
            max_core_count = core_count
            min_wire_length = wire_length

        elif core_count == max_core_count:
            min_wire_length = min(min_wire_length, wire_length)
        return
    
    x, y = coordinates[depth][0], coordinates[depth][1]

    for dir in range(4):
        length = can_connect(dir, x, y)
        if length: # 갈 수 있으면
            set_wire(dir, x, y, 1)
            dfs(depth + 1, core_count + 1, wire_length + length)
            set_wire(dir, x, y, 0)

    dfs(depth + 1, core_count, wire_length)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxynos = []
    coordinates = []

    max_core_count, min_wire_length = 0, float('inf')

    for i in range(N):
        maxynos.append(list(map(int, input().split())))

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if maxynos[i][j] == 1:
                coordinates.append((i, j))

    dfs(0, 0, 0)
    print(f'#{tc} {min_wire_length}')