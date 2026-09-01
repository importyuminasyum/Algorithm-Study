def drop():
    drop_count, result = 0, 0
    for i in range(N - 1, -1, -1):
        for j in range(boxes[i]):
            drop_count = (N - 1) - i - count[j]
            result = max(result, drop_count)
            count[j] += 1
    return result

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    count = [0] * max(boxes)

    print(f'#{tc} {drop()}')