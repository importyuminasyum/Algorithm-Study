# 입력: N, M
# 도시 정보
# 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값

# 치킨집 최대, 치킨 거리의 최소
def cal_min_length(cur_node, combination):
    hx, hy = cur_node[0], cur_node[1]
    hc_length = float('inf')

    for coordinate in combination:  
        cx, cy = coordinate[0], coordinate[1]
        hc_length = min(hc_length, abs(hx - cx) + abs(hy - cy))

    return hc_length

# chicken_restaurant 수를 가지고 조합 리스트 만들기 레스토랑 수 * M 개의 이차원 리스트 생성
def comb(depth, idx): # 현재 깊이, 인덱스

    if depth == M:
        yield combination[:]
        return
    
    for i in range(idx, len(chicken_restaurant)):
        combination.append(chicken_restaurant[i])
        yield from comb(depth + 1, i + 1)
        combination.pop()
        
def dfs():
    global min_chicken_length

    # 치킨 노드
    for combination in comb(0, 0):
     # 집 좌표 - 각각이 현재 노드
        cul_chicken_length = 0
         # 조합들
        for cur_node in house:
            cul_chicken_length += cal_min_length(cur_node, combination) # 선택한 치킨 좌표에 대해서 (하나의 조합에 대해서) 도시의 치킨 거리 합 구하기
        min_chicken_length = min(cul_chicken_length, min_chicken_length) # 도시의 치킨 거리 합 중 최솟값 구하기

N, M = map(int, input().split())

min_chicken_length = float('inf')
combination = []

city_info = [
    list(map(int, input().split()))
    for _ in range(N)
]

house = []
chicken_restaurant = []

for row in range(N):
    for col in range(N):
        if city_info[row][col] == 2:
            chicken_restaurant.append((row, col))
        elif city_info[row][col] == 1:
            house.append((row, col))

dfs()

print(min_chicken_length)


