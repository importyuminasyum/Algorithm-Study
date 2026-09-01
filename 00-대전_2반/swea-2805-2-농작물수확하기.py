T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # 2차원 배열 입력 받기
    arr = [
        list(map(int, input ()))
        for _ in range(N)
    ]
    a = N // 2
    result = []
    total = 0

    for i in range(N):
        wall = abs(a - i)
        total += sum(arr[i][wall : N - wall])

    print(f"#{test_case} {total}")