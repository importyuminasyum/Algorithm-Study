def move_horizontal(arr, x, y, direction):
    moved = 0

    while 0 <= y + direction < 100 and arr[x][y + direction] == 1:
        y += direction
        moved += 1

    return y, moved


def trace_ladder(arr, x, y):
    count = 0
    direction = 0  # 0: 방향 선택(아래), -1: 왼쪽, 1: 오른쪽

    while x < 99:

        # 방향 선택 상태
        if direction == 0:

            # 왼쪽 길이 있으면 왼쪽 이동
            if y > 0 and arr[x][y - 1] == 1:
                direction = -1

            # 오른쪽 길이 있으면 오른쪽 이동
            elif y < 99 and arr[x][y + 1] == 1:
                direction = 1

            # 좌우 길이 없으면 아래 이동
            else:
                x += 1
                count += 1

        # 왼쪽 이동
        elif direction == -1:

            y, moved = move_horizontal(arr, x, y, direction)
            count += moved

            # 가로 이동 후 아래로 이동
            x += 1
            count += 1

            direction = 0

        # 오른쪽 이동
        elif direction == 1:

            y, moved = move_horizontal(arr, x, y, direction)
            count += moved

            # 가로 이동 후 아래로 이동
            x += 1
            count += 1

            direction = 0

    return count


for _ in range(1, 11):
    test_case = int(input())

    arr = [
        list(map(int, input().split()))
        for _ in range(100)
    ]

    result = []

    # 시작점 탐색
    for y in range(100):
        if arr[0][y] == 1:
            distance = trace_ladder(arr, 0, y)
            result.append((distance, y))

    # 이동거리가 최소인 시작점의 열
    answer = min(result)[1]

    print(f'#{test_case} {answer}')