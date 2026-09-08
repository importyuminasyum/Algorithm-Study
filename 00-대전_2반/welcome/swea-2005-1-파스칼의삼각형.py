T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case}")
    
    arr = [
        [0 for _ in range(N)]
        for _ in range(N)
    ]
    
    for i in range(N):
        for j in range(N):
            arr[i][0] = 1
            arr[j][j] = 1
            
            if i >= 1 and j < i:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
            
            if arr[i][j] != 0:
                print(arr[i][j], end=" ")
        print()
