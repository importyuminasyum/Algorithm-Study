T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 2차원 배열 입력 받기
    arr = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    
    move = N-M+1 # 파리채 이동횟수
    max_arr = [] * (move)

    for i in range(move):
        for j in range(move):
            sum = 0
            # 파리채 내부 이동 구현, 한번 이동할 때마다 파리채 합 배열에 저장
            for k in range(M):
                for r in range(M):
                    sum += arr[i+k][j+r]
            max_arr.append(sum)

    print(f"#{test_case} {max(max_arr)}")