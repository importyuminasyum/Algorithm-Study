from itertools import combinations

# 최소 차이 출력하기
# 각 조합에 대해서 순회하면서 시너지 합하기 - 순열
# 각 조합에 대해서 cal 받아야 할 값은 조합 쌍과 그 조합이 아닌 쌍
# A, B에 대해서 최솟값 출력하기

def cal_min_diff(A, B):
    global min_diff 
    A_synergy, B_synergy = 0, 0

    for i, j in combinations(A, 2):
        A_synergy += synergy[i][j] + synergy[j][i]

    for i, j in combinations(B, 2):
        B_synergy += synergy[i][j] + synergy[j][i]

    return abs(A_synergy - B_synergy)

T = int(input())
for tc in range(1, T+1):
    min_diff = float('inf')

    N = int(input())
    ingredients = [i for i in range(N)]

    synergy = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    for comb in combinations(range(1, N), N // 2 - 1):
        A = (0, ) + comb
        B = [ingredient for ingredient in ingredients if ingredient not in A]

        min_diff = min(min_diff, cal_min_diff(A, B))

    print(f'#{tc} {min_diff}')