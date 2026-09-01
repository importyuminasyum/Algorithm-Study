T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge_stop = list(map(int, input().split()))
    bus = 0
    result = 0
    while bus + K < N:
        for i in range(K, 0, -1):
            if bus + i in charge_stop:
                bus += i
                result += 1
                break
        else:
            result = 0
            break

    print(f'#{test_case} {result}')