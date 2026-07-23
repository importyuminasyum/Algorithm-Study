dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0 ]

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    print(f"#{test_case}")

    d = 0
    x, y = 0, 0

    arr = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]

    arr[0][0] = 1
    
    # 로직 설계

    # 1. 현재 방향으로 다음 위치 계산
    # 2. 다음 위치로 이동 가능한지 확인
    # 3. 이동 가능하면
    #    - 숫자 기록
    #    - 현재 위치 갱신
    # 4. 이동 불가능하면
    #    - 방향 전환
    #    - 새로운 다음 위치 계산2
    #    - 숫자 기록
    #    - 현재 위치 갱신1

    for k in range(2, N * N + 1):
        nx = x + dx[d]
        ny = y + dy[d]
 
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            x = nx
            y = ny

            arr[x][y] = k

        else:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            x = nx
            y = ny
            arr[x][y] = k

    for s in arr:
        print(*s)