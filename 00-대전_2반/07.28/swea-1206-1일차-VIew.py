for test_case in range(1, 11):
    N = int(input())

    result = 0
    height = list(map(int, input().split()))
    sorted_height = [0] * 5

    for i in range(2, len(height) - 2):
        sorted_height = sorted(height[i-2 : i+3], reverse=True)
        if height[i] == sorted_height[0]:
            result += sorted_height[0] - sorted_height[1]

    print(f'#{test_case} {result}')