for _ in range(1, 11):
    test_case = int(input())
    
    arr = [
        list(map(int, input().split())) for _ in range(100)
    ]
    x = 99

    for i in range(100):
        if arr[x][i] == 2:
            y = i

    while x > 0:
        arr[x][y] = 0
        if y > 0 and arr[x][y - 1] == 1:
            y -= 1
            
        elif y < 99 and arr[x][y + 1] == 1:
            y += 1
            
        elif arr[x - 1][y] == 1:
            x -= 1

    print(f'#{test_case} {y}')