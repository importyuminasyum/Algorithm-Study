'''
등산로 조성
N * N 부지에 최대한 긴 등산로

가장 높은 봉우리에서 시작해야 함
높은 지형에서 낮은 지형으로만 - 가로 or 세로
딱 한 곳을 정해 최대 k 깊이만큼 깍을 수 있음

높이를 1보다 작게 만들 수 있음

일단 지형을 깎을 수 있는 범위가 1 ~ K까지
처음에 등산로 조성할 시작점을 찾고, 등산로 길이를 확인하면서 공사 기회가 아직 남아있을 때 사용
'''

'''
1. 뭐 선택?
출발점: 가장 높은 봉우리
이동할 다음 칸: 상하좌우
공사 여부: 경로 전체에서 최대 1번

2. 제한?
다음 칸은 현재보다 낮아야 함
공사는 최대 k 깊이
공사는 한 곳만 가능

3. 선택하면 바뀌는 거?
위치가 바뀜
필요하면 다음 칸 높이
공사 사용 여부가 F -> T

4. 결국 무엇을 최대/최소화?
등산로 길이 최대화
'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c, used, length):
    global max_length

    max_length = max(max_length, length)

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc

        if not in_range(nr, nc) or visited[nr][nc]:
            continue

        if mountain[nr][nc] < mountain[r][c]:
            visited[nr][nc] = 1
            dfs(nr, nc, used, length + 1)
            visited[nr][nc] = 0

        elif not used and mountain[nr][nc] - K < mountain[r][c]:
            original = mountain[nr][nc]
            mountain[nr][nc] = mountain[r][c] - 1
            visited[nr][nc] = 1
            dfs(nr, nc, True, length + 1)
            visited[nr][nc] = 0
            mountain[nr][nc] = original

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_height = 0
    max_length = 0
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        max_height = max(max(mountain[r]), max_height)

    for r in range(N):
        for c in range(N):
            if mountain[r][c] == max_height:
                visited[r][c] = 1
                dfs(r, c, False, 1)
                visited[r][c] = 0

    print(f'#{tc} {max_length}')


            
                