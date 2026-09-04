''' 15:20까지 구상
입력 
T
N, M - map 크기, M: 한 집의 비용
map_info - 도시 정보
출력
손해를 보지 않으면서 가장 많은 집들에 제공하는 서비스 영역 / 그 영역 내 집들의 수

max_service_area = float('-inf)

K 범위 (1 ~ ?)
for k in range(1, N - 1):
k: 중앙값(center_i, center_j)에 대해서 거리가 k 미만인 영역들
    for row in range(N):
        for col in range(N):
            center_row, center_col = row, col
            in_area_count = 0
            in_area_house_count = 0

            for small_row in range(?):
                for small_col in range(?):
                    if abs(center_row - small_row) + abs(center_col - small_col) < k:
                        in_area_count += 1

                        if map_info[small_row][small_col]:
                            in_area_house += 1

            if in_area_house_count * M < in_area_count:
                max_sevice_area = max(max_service_area, in_area_house_count)
                    
    한 K에 대해서 map_info(center_i, center_j) 순회
        (center_i, center_j) 한 쌍에 대해서 거리가 k 미만인 영역들 순회
            영역의 전체 개수 세기 - in_area_count
            영역 내의 집 개수 count - in_area_house_count

            손해 계산: in_area_house_count * M(비용) <  in_area_count:
                max_sevice_area = max(max_service_area, in_area_house_count)

            손해를 보지 않을 경우에 가장 많은 집들에 제공하는 서비스 영역 갱신

max_service_area 

k=1
*
k=2
 *
***
 *
k=3
  *
 ***
*****
 ***
  *
k=4
   *
  ***
 *****
*******
 *****
  ***
   *
k=5

    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''
def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    map_info = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    max_service_area = float('-inf')

    for K in range(1, N + 2):
        operating_cost = K ** 2 + (K - 1) ** 2

        for center_row in range(N):
            for center_col in range(N):
                in_area_count = 0
                in_area_house_count = 0

                for small_row in range(center_row - K + 1, center_row + K):
                    for small_col in range(center_col - K + 1, center_col + K):
                        if in_range(small_row, small_col, N) and abs(center_row - small_row) + abs(center_col - small_col) < K:
                            in_area_count += 1

                            if map_info[small_row][small_col]:
                                in_area_house_count += 1

                if in_area_house_count * M - operating_cost >= 0:
                    max_service_area = max(max_service_area, in_area_house_count)
    
    print(f'#{tc} {max_service_area}')

