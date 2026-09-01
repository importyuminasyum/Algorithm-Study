def move_horizontal(arr, x, y, direction):
    moved = 0

    while 0 <= y + direction < 100 and arr[x][y + direction] == 1:
        y += direction
        moved += 1

    return y, moved

def trace_ladder(arr, x, y):
    count = 0
    direction = 0

    while x < 99:
        if direction == 0:
            

            if y > 0 and arr[x][y - 1] == 1:
                direction = -1
            elif y < 99 and arr[x][y + 1] == 1:
                direction = 1
            else:
                x += 1
                count += 1
        
        elif direction == -1:
            
            y, moved = move_horizontal(arr, x, y, direction)
            count += moved

            x += 1
            count += 1

            direction = 0

        elif direction == 1:
            
            y, moved = move_horizontal(arr, x, y, direction)
            count += moved

            x += 1
            count += 1
            
            direction = 0

    return count

for _ in range(1, 11):
    test_case = int(input())
    
    arr = [
        list(map(int, input().split())) for _ in range(100)
    ]
    coordinates = {}
    result = []

    # 시작 좌표 튜플 생성
    for i in range(100):
        if arr[0][i] == 1:
            coordinates[(0, i)] = 0

    # 시작 좌표 탐색하며 카운팅
    for x, y in coordinates.keys():
        coordinates[(x, y)] =trace_ladder(arr, x, y)

    print(f'#{test_case} {min(coordinates.values())}')