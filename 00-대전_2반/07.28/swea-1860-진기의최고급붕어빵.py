T = int(input())

for test_case in range(1, T + 1):
    fish = 0
    N, M, K = map(int, input().split())
    N_arr = list(map(int, input().split()))
    N_arr = sorted(N_arr)

    for i in range(len(N_arr)):
        fish = (N_arr[i] // M) * K - i
        if fish <= 0:
            result = 'Impossible'
            break
    else:
        result = 'Possible'

    print(f'#{test_case} {result}')