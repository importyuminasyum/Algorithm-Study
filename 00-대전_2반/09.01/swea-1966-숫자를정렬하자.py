T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    for _ in range(N):
        for i in range(N - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]    

    print(f"#{tc} {' '.join(map(str, numbers))}")