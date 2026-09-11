'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while in_range(nr, nc) 할 때 동안 계속 누적하면 될듯
'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    balloons = [list(map(int, input().split())) for _ in range(N)]
    max_score, min_score = 0, float('inf')

    for r in range(N):
        for c in range(N):  
            cul_score = balloons[r][c]
            cr, cc = r, c

            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc

                while in_range(nr, nc):
                    cul_score += balloons[nr][nc]
                    nr, nc = nr + dr, nc + dc

            max_score = max(cul_score, max_score)
            min_score = min(cul_score, min_score)

    print(f'#{tc} {max_score - min_score}')