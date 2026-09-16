'''
치킨집 (2) 중 M개를 고를 때, 도시의 치킨 거리(각 집과 가장 가까운 치킨집과의 거리의 합)의 최솟값
치킨집 좌표를 리스트에 담기
M개를 인덱스로 뽑기 - 조합

집 좌표 - 치킨집 좌표 간의 거리 이차원 배열 만들기
0번 치킨집 - 0번 집 간의 거리 -  dist 배열에 넣기

그 뽑은 인덱스들에 대해서
집에 대해서 가장 가까운 거리의 치킨집을 뽑기
0번 치킨집과 뽑은 인덱스 인덱싱해서 그 중 최솟값 뽑기

최솟값 합치기 - 출력
'''

from itertools import combinations

def cal_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

N, M = map(int, input().split())
city = [list(input().split()) for _ in range(N)]

homes, chicken_restaurants = [], []

for r in range(N):
    for c in range(N):
        if city[r][c] == '1':
            homes.append((r, c))
        if city[r][c] == '2':
            chicken_restaurants.append((r, c))

h, c = len(homes), len(chicken_restaurants)
dist = [[0] * c for _ in range(h)]

for i in range(h):
    for j in range(c):
        dist[i][j] = cal_dist(homes[i][0], homes[i][1], chicken_restaurants[j][0], chicken_restaurants[j][1])

result = float('inf')
for comb in combinations(range(c), M):
    chicken_distance = 0
    for r in range(h):
        min_distance = float('inf')
        for c_i in comb:
            min_distance = min(dist[r][c_i], min_distance)
        chicken_distance += min_distance  
    result = min(result, chicken_distance)      
    
print(result)