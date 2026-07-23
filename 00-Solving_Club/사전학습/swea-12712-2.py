# 파리퇴치3

# calc: 파리채에서 + 또는 x 방향으로 M번 분사되는 영역의 합을 구하는 함수
def calc(arr, i, j, dirs, M):
    total = arr[i][j]
    N = len(arr)

    for dx, dy in dirs:
        for dist in range(1, M):
            nx = i + dx * dist
            ny = j + dy * dist

            if 0 <= nx < N and 0 <= ny < N:
                total += arr[nx][ny]

    return total
        
cross = [(-1, 0), (0, 1), (1, 0), (0, -1)]
diag = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

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

    # arr 배열의 각 영역에서 그 영역을 중심으로 M만큼 퍼진 영역의 합계를 구하고, 최댓값을 구하는 방식
    for i in range(N):
        for j in range(N):
            cross_sum = calc(arr, i, j, cross, M)
            diag_sum = calc(arr, i, j, diag, M)

            result = max(result, cross_sum, diag_sum)

    print(f"#{test_case} {result}")  
