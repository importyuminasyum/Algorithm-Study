def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def dfs(depth, used, length):
    global min_length, min_used

    if depth == N:
        if used < min_used:
            min_length = length
            min_used = used

        elif used == min_used:
            min_length = min(min_length, length)

        return

    cr, cc, dist = rcs[depth]
    # 집에서부터 충전소 설치 가능 지점 확인
    for r in range(cr - dist, cr + dist + 1):
        for c in range(cc - dist, cc + dist + 1):
            # 집에서 떨어진 거리가 범위 내인 모든 곳에 대해서
            if 0 < distance(cr, cc, r, c) <= dist:
                if (r, c) in charger:
                    dfs(depth + 1, used, length + distance(cr, cc, r, c))
                    continue

                # 충전소 없음
                # 남은 횟수 있나 보기
                # 있으면 충전소 하나 만들어
                if used < 2:
                    charger.append((r, c))
                    dfs(depth + 1, used + 1, length + distance(cr, cc, r, c))
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

    if min_length == float('inf'):
        min_length = -1

    dfs(0, 0, 0)

    print(f'#{tc} {min_length}')