def check1():
    # 내가 볼 범위, 즉 최대 개수
    for i in range(N, 1, -1):
        # 그 범위 안 인덱스
        for j in range(N - i + 1):
            if skills[j] - skills[j + i - 1] <= K:
                return i
            
    return 1

def check2():
    # 내가 볼 범위, 즉 최대 개수
    result = 0
    left = 0

    for right in range(N):
        # 그 범위 안 인덱스
        while skills[right] - skills[left] > K:
            left += 1

        result = max(result, right - left + 1)

    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    skills = list(map(int, input().split()))
    skills.sort()

    print(f'#{tc} {check1()} {check2()}')

