# 입력: N, M
# 도시 정보
# 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값

# 치킨집 최대, 치킨 거리의 최소
def cal_min_length(cur_node, chicken_restaurants):
    hx, hy = cur_node[0], cur_node[1]
    hc_length = float('inf')

    for restaurant in chicken_restaurants:  
        cx, cy = restaurant[0], restaurant[1]
        hc_length = min(hc_length, abs(hx - cx) + abs(hy - cy))

    return hc_length

# chicken_restaurant 수를 가지고 조합 리스트 만들기 레스토랑 수 * M 개의 이차원 리스트 생성
def comb(depth, idx): # 현재 깊이, 인덱스

    if depth == M:
        comb_combinations.append(combinations[:])
        return
    
    for i in range(idx, len(chicken_restaurant)):
        combinations.append(chicken_restaurant[i])
        comb(depth + 1, i + 1)
        combinations.pop()
        
def dfs():
    global min_chicken_length

    comb(0, 0)
    # 치킨 노드
    for i in range(len(comb_combinations)):
     # 집 좌표 - 각각이 현재 노드
        chicken_length = 0
         # 조합들
        for cur_node in house:
            chicken_length += cal_min_length(cur_node, comb_combinations[i]) # 도시의 치킨 거리 합 구하기
        min_chicken_length = min(chicken_length, min_chicken_length) # 

N, M = map(int, input().split())
min_chicken_length = float('inf')
combinations = []
comb_combinations = []

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
