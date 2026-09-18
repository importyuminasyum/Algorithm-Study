
# 연관 문제 - 모의 역량 테스트 SWEA
# 농작물 수확하기(멘헤튼) - distance, 홈 방범 서비스, 무선충전, 프로세서 연결하기

def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def dfs(depth, used, length):
    global min_length, min_used

    # 가지치기(시간복잡도 줄이기 용)
    # 이미 찾은 최소 충전소 개수보다 많이 사용한 경우 탐색 중단
    if used > min_used:
        return
    
    # 가지치기(시간복잡도 줄이기 용)
    # 충전소 개수가 같고 현재 거리 합도 이미 최소값 이상이면
    # 이후 거리는 증가만 하므로 탐색 중단
    if used == min_used and length >= min_length:
        return

    # 종료 조건
    if depth == N:
        if used < min_used:
            min_length = length
            min_used = used

        elif used == min_used:
            min_length = min(min_length, length)

        return

    cr, cc, dist = rcs[depth]

    # 현재 집의 충전 가능 거리 안에 있는 모든 충전소 후보 좌표 탐색
    for r in range(cr - dist, cr + dist + 1):
        for c in range(cc - dist, cc + dist + 1):
            d = distance(cr, cc, r, c)
            
            # 현재 집 위치 자체는 제외하고, 충전 가능 거리 이내의 좌표만 사용
            if not 0 < d <= dist:
                continue

            # 다른 집의 위치에도 충전소를 설치할 수 없음
            if (r, c) in house_positions:
                continue
            
            # 충전소 있음
            if (r, c) in charger:
                dfs(depth + 1, used, length + d)
                continue

            # 설치된 충전소가 없다면, 최대 2개까지 새 충전소 설치
            if used < 2:
                charger.append((r, c))
                dfs(depth + 1, used + 1, length + d)
                charger.pop()
                continue

            # 남은 횟수 없는데 충전소도 없음 - 이 경로는 폐기
            continue

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rcs = []
    charger = []
    min_length, min_used = float('inf'), float('inf')
    for _ in range(N):
        y, x, dist = map(int, input().split())
        r, c = x + 15, y + 15
        rcs.append((r, c, dist))

    house_positions = {(r, c) for r, c, _ in rcs}

    dfs(0, 0, 0)

    if min_length == float('inf'):
        min_length = -1

    print(f'#{tc} {min_length}')
