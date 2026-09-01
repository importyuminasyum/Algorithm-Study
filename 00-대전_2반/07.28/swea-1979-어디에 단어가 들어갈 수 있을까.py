def count_wordspace(arr, K):
    count = 0
    target = [1] * K
    for i in range(len(arr) - K + 1):
        if arr[i : i + K] == target:
            if (i == 0 or arr[i - 1] == 0) and (i + K == len(arr) or arr[i + K] == 0):
                count += 1
    return count

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    count = 0
    arr = [
        list(map(int, input().split())) for _ in range(N)
    ]
    
    for i in range(N):
        count += count_wordspace(arr[i], K)
        col_arr = []
        for j in range(N):
            col_arr.append(arr[j][i])
        count += count_wordspace(col_arr, K)
    print(f'#{test_case} {count}')
