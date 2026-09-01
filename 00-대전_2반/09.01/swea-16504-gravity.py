def drop():
    result = 0

    for i in range(N - 1):
        smaller_count = 0

        for j in range(i + 1, N):
            if boxes[i] > boxes[j]:
                smaller_count += 1

        result = max(result, smaller_count)

    return result

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    boxes = list(map(int, input().split()))

    print(f'#{tc} {drop()}')