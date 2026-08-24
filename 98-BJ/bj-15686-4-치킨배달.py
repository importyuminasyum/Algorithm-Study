# 입력: N, M
# 도시 정보
# 폐업시키지 않을 치킨집을 최대 M개 선택, 도시의 치킨 거리의 최솟값 출력
# 일단 치킨집과 집의 좌표 저장
# 치킨집을 M개 선택해야 하므로, 조합으로 하나씩 뽑기 - [(), (), ()] 이런식
# 치킨집과 집 간의 거리들을 다 계산해놓기
# distance[house_idx][chicken_idx]
# 각 집과 각 치킨집 사이의 거리를 저장
# 그래서 도시의 치킨 거리의 최솟값은 각 distance들의 합의 최솟값
from itertools import combinations

N, M = map(int, input().split())

min_chicken_length = float('inf')
city_info = [
    list(map(int, input().split()))
    for _ in range(N)
]

house, chicken_restaurant = [], []
for row in range(N):
    for col in range(N):
        if city_info[row][col] == 1:
            house.append((row, col))
        elif city_info[row][col] == 2:
            chicken_restaurant.append((row, col))

distance = [
    [0] * len(chicken_restaurant)
    for _ in range(len(house))
]

for row in range(len(house)):
    for col in range(len(chicken_restaurant)):
        distance[row][col] = abs(house[row][0] - chicken_restaurant[col][0]) + abs(house[row][1] - chicken_restaurant[col][1])

for comb in combinations(range(len(chicken_restaurant)), M):
    chicken_length = 0

    for house_idx in range(len(house)):

        current_min_length = min(
            distance[house_idx][chicken_index]
            for chicken_index in comb
        )       
        chicken_length += current_min_length

        if chicken_length >= min_chicken_length:
            break

    min_chicken_length = min(min_chicken_length, chicken_length)

print(min_chicken_length)