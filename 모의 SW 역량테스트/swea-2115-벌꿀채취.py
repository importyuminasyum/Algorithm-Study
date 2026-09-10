'''
10
4 2 13
6 1 9 7    
9 8 5 8
3 4 5 3
8 2 6 7
'''

'''
입력: 벌통 크기 N, 선택 가능한 벌통 개수 M, 꿀을 채취할 수 있는 최대 양 C
입력: 벌통들 N * N - 각 칸의 숫자: 꿀의 양
하나의 벌통에서 일부분의 꿀만 채취할 수 없음, 모든 꿀 한 번에 채취

1. 두 명의 일꾼이 꿀을 채취할 수 있는 벌통의 수 M: 2, 
가로로 연속되도록 M개의 벌통 선택, 선택한 벌통들에서 꿀 채취
단, 겹치면 안 됨

2. 두 명의 일꾼은 선택한 벌통에서 꿀을 채취하여 용기에 담기
서로 다른 벌통에서 채취한 꿀이 섞이게 되면 상품 가치가 떨어짐, 하나의 벌통에서 채취한 꿀은 하나의 용기에 담아야 함 
하나의 벌통에서 꿀을 채취할 때, 일부분만 채취할 수 없고 벌통에 있는 모든 꿀을 한 번에 채취해야함
두 일꾼이 채취할 수 있는 꿀의 최대 양 C: 13 

3. 하나의 용기에 있는 꿀의 양이 많을수록 상품 가치가 높아, 각 용기에 있는 꿀의 양의 제곱만큼의 수익이 생김
수익은 각 꿀통의 꿀의 양의 제곱의 합: 만약 6, 1, 8을 선택했다면 수익은 6*6 + 1*1 + 8*8 = 101
    
완전탐색

1) N * N에서 1 * M개 크기의 벌통 2개를 선택하는 조합
- visited[N][N - M + 1] 선언
- 겹치면 안 됨
- 일단 범위 N * (N - M + 1) 의 좌표를 순회하면서
- 배열 2개 골라야 함
- select1 = [r][c] 고르기
- 고르고 방문 처리 어떻게?
- visited[r][c] = 1
- dfs()로 고른 담에 보내기
- depth == 2 면 다 뽑았으니까 그거 가지고 2) 시작
- 인덱스 선택
- 다음 와서는 그 인덱스 값이 체크 되어 있는지, 그 값의 절댓값의 차이
- select1의 행 값과 같으면 c 비교 (select1의 c값과 select2의 c값의 절댓값의 차이(거리)가 M보다 작으면 겹친다는 뜻, 고르지 마)
- select2 = [r][c] 고르기

visited = [[0] * (N - M + 1) for _ in range(N)]
comb(depth):
    global answer
    if depth == 2:
        answer = max(answer, cal_profit(hive_selection))
        return

    for r in range(N):
        for c in range(N - M + 1):
            if hive_seleciton and (visited[r][c] or abs(c - hive_selection[-1][1]) < M:
                continue
                
            hive_selection.append((r, c))
            visited[r][c] = 1
            dfs(depth + 1)
            hive_selection.pop()
            visited[r][c] = 0


2) 조합 선택한 후에 가능한지 확인
- select1 에서 고른 좌표 한 쌍으로 순회
- 내가 고른 두 좌표들의 각 벌통의 합을 확인하고 가장 많이 꿀을 채취할 수 있는 양을 저장해야 함 왜? - 그게 그 조합의 최대 수익의 합
- 그럼 나는 두 좌표에서 고른 벌통을 리스트로 모을까? 그 값이 만약에 C보다 크면 그 중에서 최솟값인 애를 버리고 확인하기
- 되는 순간 그거 가지고 수익을 확인할 수 있게 되고, 그걸 전체 출력 최대수익으로 갱신하기
def cal_profit(selected_hive):
    max_profit = 0
    honey_volume1, honey_volume2 = [], []
    for idx in range(2):
        for r, c in selected_hive[idx]:
            for i in range(c, c + M):
                honey_volume1.append(selected_hive[r][i])
                honey_volume2.append(selected_hive[r][i])

    if sum(honey_volume1) > c or sum(honey_volume) > c:
        return max_profit

    honey_volume = honey_volume1 + honey_volume2
    honey_volume.sort(reverse = True)

    while len(honey_volume) > 1:
        if sum(honey_volume) <= c:
            max_profit = sum([x ** 2 for x in honey_volume])
            return
        
        honey_volume.pop()

    return max_profit

    

출력: 두 일꾼이 꿀을 채취하여 얻을 수 있는 최대 수익
'''

def comb(depth, start):
    global answer
    if depth == 2:
        answer = max(answer, cal_profit(hive_selection))
        return

    for i in range(start, len(candidates)):
        r, c = candidates[i]

        if hive_selection:
            prev_r, prev_c = hive_selection[-1]

            if prev_r == r and abs(c - prev_c) < M:
                continue
            
        hive_selection.append((r, c))
        comb(depth + 1, i + 1)
        hive_selection.pop()

def cal_profit(selected_hive):
    max_profit = 0
    honey_volume1, honey_volume2 = [], []
    
    r, c = selected_hive[0]
    for i in range(c, c + M):
        honey_volume1.append(beehives[r][i])
    r, c = selected_hive[1]
    for i in range(c, c + M):
        honey_volume2.append(beehives[r][i])

    sum1, sum2 = sum(honey_volume1), sum(honey_volume2)
    honey_square_profit1 = sum([x ** 2 for x in honey_volume1])
    honey_square_profit2 = sum([x ** 2 for x in honey_volume2])

    if sum1 <= C and sum2 <= C:
        max_profit = honey_square_profit1 + honey_square_profit2
        return max_profit

    if sum1 > C:
        honey_square_profit1 = cal_max_square_subset_sum_list(0, honey_volume1, 0, 0)

    if sum2 > C:
        honey_square_profit2 = cal_max_square_subset_sum_list(0, honey_volume2, 0, 0)

    max_profit = honey_square_profit1 + honey_square_profit2

    return max_profit

def cal_max_square_subset_sum_list(depth, honey_volume, cur_square_sum, cur_sum):
    if cur_sum > C:
        return 0

    if depth == len(honey_volume):
        return cur_square_sum

    pick_square_sum = cal_max_square_subset_sum_list(depth + 1, honey_volume, cur_square_sum + honey_volume[depth] ** 2, cur_sum + honey_volume[depth])
    no_pick_square_sum = cal_max_square_subset_sum_list(depth + 1, honey_volume, cur_square_sum, cur_sum)

    if pick_square_sum > no_pick_square_sum:
        return pick_square_sum
    else:
        return no_pick_square_sum



T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    beehives = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * (N - M + 1) for _ in range(N)]
    answer = 0

    hive_selection = []
    candidates = []
    for r in range(N):
            for c in range(N - M + 1):
                candidates.append((r, c))

    comb(0, 0)

    print(f'#{tc} {answer}')

