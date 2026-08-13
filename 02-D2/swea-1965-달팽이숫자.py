def in_range(row, col, N):
    return 0 <= row < N and 0 <= col < N

# 달팽이 배열
# 총 N번 반복
# 출발 (->)
# 다음 좌표 확인
# 범위 밖이면
# 방향 바꾸기
# 가기
# 다음 좌표에 숫자가 들어있으면
# 방향 바꾸기

def snail_nums(N):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 왼, 상
    dir = 0 # 방향 인덱스 nx, ny = dirs[dir][0], dirs[dir][0] 형태
    # 초기 배열 설정
    x, y = 0, 0 
    arr[x][y] = 1

    for num in range(2, N * N + 1):
        # 다음 좌표 확인
        nx, ny = x + dirs[dir][0], y + dirs[dir][1]
        # 가능하면
        if in_range(nx, ny, N) and arr[nx][ny] == 0:
            # 가기
            x, y = nx, ny
            arr[x][y] = num
        # 아니면  
        # 방향 바꾸기
        else:
            dir = (dir + 1) % 4

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    print(f'#{tc}')

    snail_nums(N)
    for i in range(N):
        print(*arr[i])