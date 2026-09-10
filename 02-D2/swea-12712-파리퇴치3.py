'''
파리를 한 번만 뿌려 최대한 많은 파리를 잡으려고 함
스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 
M 칸의 파리를 잡을 수 있음
한 번에 잡을 수 있는 최대 파리 수

입력 
T
N, M: 배열 크기, 세기

max_flies 출력

dirs1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

중심칸(N*N)을 돌면서 M 세기로 분사했을 때의 모든 방향에 대한 sum 값을 저장해야 함
그걸 max 갱신

max - 십자가, 대각선 sum 값도 비교해야 함
sum1, sum2 만들어놓고 max(max_flies, sum1, sum2)

for r in range(N):
    for c in range(N):
        cr, cc = r, c
        sum1, sum2 = field[cr][cc], field[cr][cc]
        for length in range(1, M):
            for dr, dc in dirs1:
                nr, nc = cr + dr * length, cc + dc * length
                if not in_range(nr, nc):
                continue
                sum1 += field[nr][nc]

            for dr, dc in dirs2:
                nr, nc = cr + dr * length, cc + dc * length
                if not in_range(nr, nc):
                continue
                sum1 += field[nr][nc]

        max_flies = max(max_flies, sum1, sum2)
'''   
dirs1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dirs2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0

    for r in range(N):
        for c in range(N):
            cr, cc = r, c
            sum1, sum2 = field[cr][cc], field[cr][cc]
            for length in range(1, M):
                for dr, dc in dirs1:
                    nr, nc = cr + dr * length, cc + dc * length
                    if not in_range(nr, nc):
                        continue
                    sum1 += field[nr][nc]

                for dr, dc in dirs2:
                    nr, nc = cr + dr * length, cc + dc * length
                    if not in_range(nr, nc):
                        continue
                    sum2 += field[nr][nc]

            max_flies = max(max_flies, sum1, sum2)

    print(f'#{tc} {max_flies}')