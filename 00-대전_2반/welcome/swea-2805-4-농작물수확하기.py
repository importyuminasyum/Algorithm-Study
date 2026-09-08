# 중간에서부터 떨어진 거리가 n // 2 이내인 값들의 합 출력
T = int(input())
for tc in range(1, T+1):
    answer = 0

    N = int(input())
    field = []
    crops = [(input()) for _ in range(N)] 

    mid = distance = N // 2
    
    for r in range(N):
        for c in range(N):
            if abs(mid - r) + abs(mid - c) <= distance:
                answer += int(crops[r][c])

    print(f'#{tc} {answer}')