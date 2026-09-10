'''
8방향 탐색
예비 후보지를 정하려 하는데, 8개 방형 중 사진을 찍을 수 있는 방향이
4방향 이상인 지점이 예비 후보지가 될 수 있음
착륙지점보다 높이가 낮은 구역의 사진을 찍을 수 있음
T
N, M: 행, 열
A: 높이정보
'''
dirs = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]
    candidates_count = 0

    for r in range(N):
        for c in range(M):
            cr, cc, height = r, c, heights[r][c]
            photo_count = 0

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                if not in_range(nr, nc):
                    continue

                if heights[nr][nc] < height:
                    photo_count += 1

            if photo_count >= 4:
                candidates_count += 1

    print(f'#{tc} {candidates_count}')