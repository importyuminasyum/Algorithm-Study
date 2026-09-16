'''
방향 전환이 여러 분기

1. 뭐 선택?
시작지점에서

dir에 따라
다음 방향을 꺾을 지점
- 총 세 번 꺾어야 함
- dir 0, 2 이면 a
- dir 1, 3 이면 b

2. 제약 조건은?
범위 내 - in_range
같은 숫자의 디저트를 파는 카페가 있으면 안됨 - 겹치면 그냥 끝 - set
하나의 카페에서 도는 것도 안 됨 - 도는 건 무조건 한 칸 이상 가서
왔던 길 돌아가는 것도 안 됨 - 방문 처리
백트래킹

3. 선택하면 바뀌는 거?
현재 위치
지금까지 선택한 디저트
(r, c, a, b, selected)

4. 뭐에 대한 최대?최소?
len(selected)의 최대
'''
dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c, dir, selected):
    global max_dessert

    for nd in range(dir, min(dir + 2, 4)):
        nr, nc = r + dirs[nd][0], c + dirs[nd][1]

        if not in_range(nr, nc):
            continue

        if nr == start_r and nc == start_c:
            if nd == 3:
                max_dessert = max(max_dessert, len(selected))
            continue

        if visited[nr][nc]:
            continue

        if cafe[nr][nc] in selected:
            continue

        visited[nr][nc] = 1
        selected.add(cafe[nr][nc])
        dfs(nr, nc, nd, selected)
        visited[nr][nc] = 0
        selected.remove(cafe[nr][nc])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    max_dessert = -1
    selected = set()

    for r in range(N):
        for c in range(N):
            start_r, start_c = r, c
            visited[r][c] = 1
            selected.add(cafe[r][c])
            dfs(start_r, start_c, 0, selected)
            visited[r][c] = 0
            selected.remove(cafe[r][c])

    print(f'#{tc} {max_dessert}')
