# 입력: N, M
# 도시 정보
# 폐업시키지 않을 치킨집을 최대 M개 골랐을 때, 도시의 치킨 거리의 최솟값
# chicken_restaurant 수를 가지고 조합 리스트 만들기 레스토랑 수 * M 개의 이차원 리스트 생성
def comb(depth, idx): # 현재 깊이, 인덱스
    
    if depth == M:
        yield combination[:]
        return
    
    for i in range(idx, len(chicken_restaurant)):
        combination.append(i)
        yield from comb(depth + 1, i + 1)
        combination.pop()
        
def calculate_min_distance():
    global min_chicken_length

    # 치킨 노드
    for combination in comb(0, 0):
     # 집 좌표 - 각각이 현재 노드
        cul_chicken_length = 0
        # 조합들
        for h in range(len(house)):
            min_length = float('inf')
            for c in combination:
                min_length = min(min_length, distance[h][c])
            cul_chicken_length += min_length        
        # 선택한 치킨 좌표에 대해서 (하나의 조합에 대해서) 도시의 치킨 거리 합 구하기
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

distance = [ [0 for _ in range(len(chicken_restaurant))]  for _ in range(len(house)) ]
    
for h in range(len(house)):
    for c in range(len(chicken_restaurant)):
            distance[h][c] = abs(house[h][0] - chicken_restaurant[c][0]) + abs(house[h][1] - chicken_restaurant[c][1])

calculate_min_distance()
print(min_chicken_length)


