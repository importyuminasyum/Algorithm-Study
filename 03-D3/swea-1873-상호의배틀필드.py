# 상, 우, 하, 좌
dx, dy = (-1, 0, 1, 0), (0 ,1, 0, -1)

# 숫자로 치환
direction = {
    '^': 0,
    '>': 1,
    '<': 3,
    'v': 2,
    'U': 0,
    'R': 1,
    'L': 3,
    'D': 2,
    }

# 탱크 확인
def is_tank(sgchar):
    return sgchar in '^><v'

def dir_tank_to_num(sgchar):
    return direction[sgchar]

def dir_tank_to_char(num):
    if num == 0:
        return '^'
    if num == 1:
        return '>'
    if num == 3:
        return '<'
    if num == 2:
        return 'v'

# 범위 확인
def in_range(nx, ny, H, W):
    return 0 <= nx < H and 0 <= ny < W

# shoot 함수 - 의도: status 행렬 변경 (return 없음)
def shoot(x, y, status, dir, H, W):
    # 포탄 좌표 자체는 status 영향 없음
    nx, ny = x + dx[dir], y + dy[dir]
    while in_range(nx, ny, H, W):
        if status[nx][ny] == '#':
            break
        elif status[nx][ny] == '*':
            # 이 경우만 status 변경
            status[nx][ny] = '.'
            break
        else:
            nx, ny = nx + dx[dir], ny + dy[dir]

# move 함수 
def move(x, y, status, dir, H, W):
    # 다음 방향 좌표 업데이트
    nx, ny = x + dx[dir], y + dy[dir]
    if in_range(nx, ny, H, W) and status[nx][ny] == '.':
        # 이동 가능할 때 탱크 모양 바꿔 넣어주고 현재 좌표 평지화 (이동)
        status[nx][ny] = dir_tank_to_char(dir)
        status[x][y] = '.'
        # 현재 좌표 변경
        x, y = nx, ny
    else:
        # 이동 불가능해도 방향은 바뀌었으니 탱크 모양 바꿔줌
        status[x][y] = dir_tank_to_char(dir)
    return x, y

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    status = []
    for _ in range(H):
        status.append(list(input()))

    N = int(input())
    commands = list(input())

    # 초기 탱크 위치 좌표, 방향 탐색
    for i in range(H):
        for j in range(W):
            if is_tank(status[i][j]):
                dir = dir_tank_to_num(status[i][j])
                x, y = i, j

    # shoot은 return 업어도 됨
    # move는 이동 후 탱크 좌표, 방향 재할당 필요
    for command in commands:
        if command == 'S':
            shoot(x, y, status, dir, H, W)
        else:
            dir = dir_tank_to_num(command)
            x, y = move(x, y, status, dir, H, W)

    print(f'#{tc}', end=' ')
    for row in range(H):
        # 붙여서 출력
        print(''.join(status[row]))