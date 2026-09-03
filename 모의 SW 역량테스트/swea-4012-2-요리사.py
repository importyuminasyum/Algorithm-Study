def cal_diff(A, B):
    taste1, taste2 = 0, 0

    for i, j in combinations(A, 2):
        taste1 += synergy[i][j] + synergy[j][i]

    for i, j in combinations(B, 2):
        taste2+= synergy[i][j] + synergy[j][i]

    return abs(taste1 - taste2)

from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    min_diff = float('inf')
    numbers_set = set(i for i in range(N))
 
    for comb in combinations(range(1, N), N // 2 - 1):
        A = (0, ) + comb
        B = [x for x in numbers_set if x not in A]
        min_diff = min(min_diff, cal_diff(A, B))

    print(f'#{tc} {min_diff}')

    # 조합 정하기
    # 식재료 N개 중 N//2개를 뽑는 조합의 수: 하나(인덱스) 뽑을 때 두 개의 리스트가 생겨야 비교 가능
    # 조합 뽑을 때 필요한 것: 방문 배열 - 노드에 대해서, 방문 배열 - 조합에 대해서 (왜? 같은 거 두 번 연산하지 않도록)
    # pick_numbers(set)에 N//2만큼 뽑았을때, pick_numbers2(set)에 처음 다 있던 인덱스 배열(set)과 pick_numbers(set) 차집합 연산 해서 넣기
    # 한 인덱스 조합 (리스트) - ij ji 합 : 맛
    # 다른 인덱스 조합 (리스트) - synergy[i][j] + synergy[j][i] 합 : 맛
    # pick_numbers = []

# numbers_set = set(i for i in range(N)) # comb가 뽑을 첫 숫자 인덱스 배열
# visited_idx = [0] * N
# visited_comb = [(i, j, k), ] # 지금까지 만든 조합 왜? 같은 거 두 번 하기 싫어서
# K = N//2
# def comb(depth, idx, K):
#     if len(pick_numbers1) == K:
        
#         pick_numbers2 = numbers_set - pick_numbers1

#         visited_comb.append(pick_numbers1)
#         visited_comb.append(pick_numbers2)
#         return cal_diff(pick_numbers1, pick_numbers2)

#     for i in range(N):
#         pick_numbers1.add(numbers_set[i])
#         comb(depth + 1, idx + 1)
#         pick_numbers1.pop()

