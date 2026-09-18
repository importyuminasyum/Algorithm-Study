import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = list(map(int, input().split()))
    diff, min_length = [], []
    result = [0, 0]
    for height in heights:
        max_height = max(heights)
        if height == max_height:
            continue
        diff.append(max_height - height)

    for d in diff:
        result[0] += d % 2
        result[1] += d // 2

    while result[1] > result[0] + 1:
        result[0] += 2
        result[1] -= 1

    answer = sum(result)

    print(f'#{tc} {max(result[0] * 2 - 1, result[1] * 2)}')