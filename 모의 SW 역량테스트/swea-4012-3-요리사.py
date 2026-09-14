from itertools import combinations

def cal_min_diff(A, B):
    A_taste, B_taste = 0, 0
    for i, j in combinations(A, 2):
        A_taste += synergy[i][j] + synergy[j][i]

    for i, j in combinations(B, 2):
        B_taste += synergy[i][j] + synergy[j][i]

    return abs(A_taste - B_taste)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')

    for comb in combinations(range(1, N), N // 2 - 1):
        A  = (0, ) + comb
        B = set(i for i in range(N) if i not in A)

        min_diff = min(cal_min_diff(A, B), min_diff)

    print(f'#{tc} {min_diff}')
    
