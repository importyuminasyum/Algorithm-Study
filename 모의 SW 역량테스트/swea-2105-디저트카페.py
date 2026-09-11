'''
디저트 카페
N * N 디저트 카페들이 있음
값: 디저트의 종류
대각선 방향으로 움직일 수 있음
어느 한 카페에서 출발해서 대각선 방향으로 움직이고 사각형 모양을 그리면서 출발한 카페로 돌아와야 함
카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 됨
- 또 나오면 제껴
- 하나의 카페에서 디저트를 먹는 것도 안 됨
- 왔던 길을 다시 돌아가는 것도 안 됨

- 디저트를 되도록 많이 먹으려고 함
T
N
N * N - 디저트 종류

출력
max_dessert
- 디저트를 가장 많이 먹을 때의 디저트 수
- 디저트를 먹을 수 없는 경우 -1

일단 방향을 바꿔
- 중심에서
dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

중심에서 투어 시작인데 
- 범위는 행은 끝에서 2 전까지만 가능 range(N - 3)
- 열은 처음 열 끝 열은 제외 range(1, N - 1) 

중심 탐색
- 한 중심에 대해서
cr, cc = r, c

for dir in range(4):
    중심에서부터 끝 인덱스까지의 차: N - 1 - r
    그만큼 length로 두기 - 한 dir에 대해서 최대 그만큼만 반복 가능
    length_range = N - r
    for length in range(1, length_range):

        dr, dc = dirs[dir][0], dirs[dir][1]
        nr, nc = cr + dr * length, cc + dc * length

        if not in_range(nr, nc): - 범위 벗어나면 자리 바꿔
            continue
            
        if rocation[nr][nc] - 이미 먹은 적 있으면 그 방향 그만 봐(set으로 관리)
            break
        
        visited_dessetadd(rocation[nr][nc])
        
        도달하는 것까지는 어떻게 구현하겠는데
        범위가 안 되도 그냥 가고 싶은데
        max_dessert = max(len(dessert), max_dessert)
    

'''