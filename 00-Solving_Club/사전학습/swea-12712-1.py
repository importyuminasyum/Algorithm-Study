dx1 = [-1, 0, 1, 0]
dy1 = [0, -1, 0, 1]
dx2 = [-1, 1, 1, -1]
dy2 = [-1, -1, 1, 1]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0

    # 2차원 배열 입력 받기
    arr = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    for i in range(N):
        for j in range(N):
            centerx, centery = i, j
            result1, result2 = arr[i][j], arr[i][j]

            for k in range(4):
                for s in range(1, M):
                    nx1 = centerx + dx1[k] * s
                    ny1 = centery + dy1[k] * s
                    nx2 = centerx + dx2[k] * s
                    ny2 = centery + dy2[k] * s

                    if 0 <= nx1 < N and 0 <= ny1 < N:
                        result1 += arr[nx1][ny1]

                    if 0 <= nx2 < N and 0 <= ny2 < N:
                        result2 += arr[nx2][ny2]

            result = max(result, result1, result2)
                    
    print(f"#{test_case} {result}")