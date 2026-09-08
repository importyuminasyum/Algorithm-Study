# 횟수 맞추고 시작점 조율 (평행이동)
T = int(input())
for tc in range(1, T+1):
    answer = 0

    N = int(input())
    field = []
    crops = [(input()) for _ in range(N)] 

    mid = N // 2
    
    for r in range(N):
        for c in range(abs(mid-r), N-2*(abs(mid-r))+abs(mid-r)):
            answer += int(crops[r][c])

    print(f'#{tc} {answer}')