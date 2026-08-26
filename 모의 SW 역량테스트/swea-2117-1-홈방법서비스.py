# 한 k에 대해서 cost 계산 - 동일
# 만약 현재 k값의 비용이 누적 최대 집 개수보다 작아지면 종료 
# - 이후 탐색 시 k안에 모든 집으로 차있어도 더이상 누적 최대 집보다 커질 수 없음

# 센터 값 지정하면서 k, 격자 내 한 센터와 비용에 대해서 주변 거리를 탐색하면서 k 거리 내에 있는 집들의 개수를 세가
# 손해가 아닐 때만 집 개수 return, 아니면 0
# 누적 최대 집 개수 업데이트

def cal_max_house():
    global max_house

    for k in range(1, N + 2):
        cost = k * k + (k - 1) * (k - 1)

        # i, j : center 값
        for i in range(N):
            for j in range(N):
                max_house = max(max_house, cal_house(k, i, j, cost)) # center 값 기준으로 돌면서 거리 탐색

def cal_house(k, i, j, cost): # 손해인지 아닌지, house 수
    house = 0

    for r in range(N):
        for c in range(N):
            if abs(i - r) + abs(j - c) < k and city[r][c]:
                house += 1

    if house * M >= cost:
        return house
            
    else:
        return 0

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    max_house = 1

    city = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    cal_max_house()

    print(f'#{tc} {max_house}')