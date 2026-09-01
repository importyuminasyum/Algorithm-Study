for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    household = 0

    for i in range(2, N - 1):
        slicing_heights = sorted(heights[i - 2:i + 3])
        if heights[i] == slicing_heights[0]:
            household += heights[i] - slicing_heights[1]

    print(f'#{tc} {household}')