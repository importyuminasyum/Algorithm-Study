# 초기 배열 생성해서 입력 받기
# deepcopy해서 한 번 트라이마다 - 모든 노드 다 돌 때마다 사용하고 초기화 할 것
# 결과 담을 count - 한 번 트라이마다 최솟값 갱신
# 1~n-1, 1~n-1 확인한다음 coordinates에 튜플로 x, y 담기
# 출력: 모든 트라이에서 최솟값

# def 함수 정의 인자: node (depth, count)
# 종료조건: node 가 끝났을 때
# 전원이 연결되지 않는 core가 존재할 수 있음?
# global total_count 선언
# x, y = coordinates[node][0], coordinates[node][1] 일단 현재 좌표부터 정하기(노드)
# 종료조건: node 가 coordinates 행길이 + 1과 같을 때 종료, 이때 복사한 배열 초기화해야 함, 
# total count 리턴 
# total_count = min(count, total_count)

# 아무래도 while dir < 4: 이거 넣는 게 좋을 듯
# dir <- 0 (우), 1(하), 2(좌), 3(상)
# if dir % 2 == 0: 이면 열을 봐야함 이때는 count += abs(y - j) # 우 abs(y) # 좌
# if dir % 2 == 0: 이면 행을 봐야함 이때는 count += abs(x - i) # 하 abs(x) # 상

# for col in range(N)
# 돌면서 - 갈 수 있는 경우에 그 전선 수를 더해줘야 함
# 일단 dx, dy ? 할지 말지 결정하는데
# 일단 방향 잡아 계속 가면서 1이 있는지 확인 - 있으면 바로 방향 바꾸기 후 continue
# 다 돌아버리면: 그 간 만큼을 전선에 넣을 건데 이거 dfs
# count에 뭘 넣을 건데? 갈 수 있었을 때의 i, j 든 이것과 x, y 간의 절댓값 = 전선 길이
# else 하나 더 넣어야 함 그래도 돌려야 함 왜? 3. 최대한 많은 Core에 전원을 연결해도, 전원이 연결되지 않는 Core가 존재할 수 있다.
# dfs(depth + 1, count) 여태 누적 count

# dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
# dir = 0
# x + dirs[dir], y + dirs[dir] 
import copy

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) # 우하좌상

def in_range(x, y, N):
    return 0 <= x < N and 0 <= y < N

def cal_wire_length(dir, x, y, nx, ny): # 현재 방향, 끝까지 간 좌표에서 첫 좌표 빼서 리턴
    return abs(y - ny) if dir % 2 == 0 else abs(x - nx)

def dfs(cur_xy_count, count):
    global maxynos_copy, total_count

    if cur_xy_count == len(coordinates):
        maxynos_copy = copy.deepcopy(maxynos)
        total_count = max(total_count, count)
        count = 0
        return

    x, y = coordinates[cur_xy_count][0], coordinates[cur_xy_count][1]
    
    for dir in range(4): # 한 방향에 대해서
        mul = 1
        nx, ny = x + dirs[dir][0] * mul, y + dirs[dir][1] * mul # 한 번 더한 거 / 근데 여러 번 더해야 함

        while in_range(nx, ny, N):
            if maxynos_copy[nx][ny] == 0: # 갈 수 있으면
                maxynos_copy[nx][ny] = 1 # 가고 방문처리
                nx, ny = x + dirs[dir][0] * mul, y + dirs[dir][1] * mul # ... 칸 더 가기 
                mul += 1 
            else: # 갈 수 없으면
                break # 그 방향으로는 안 가
        else: # break 가 안 떴다? 그 방향으로 끝까지 갔다는 뜻, 그 때 nx, ny 중 하나 0이거나 N
            # 그 간 만큼 전선 길이 넣기
            dfs(cur_xy_count + 1, count + cal_wire_length(dir, x, y, nx, ny))
            
    dfs(cur_xy_count + 1, count)

    
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxynos = []
    coordinates = []
    total_count = 0
    for i in range(N):
        maxynos.append(list(map(int, input().split())))
    maxynos_copy = copy.deepcopy(maxynos)

    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if maxynos[i][j] == 1:
                coordinates.append((i, j))

    dfs(0, 0)
    print(f'#{tc} {total_count}')