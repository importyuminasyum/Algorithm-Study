# T
# N
# 회사 좌표, 집 좌표, N명의 고객의 좌표
# 두개씩 끊어서 저장
 
# 회사에서 이들을 모두 방문 후 집에 돌아가는 경로 중 이동거리가 가장 짧은 경로를 찾기
from itertools import permutations
 
def cal_length(bef_rc, cur_rc):
    return abs(bef_rc[0] - cur_rc[0]) + abs(bef_rc[1] - cur_rc[1])
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rcs = list(map(int, input().split()))
    customers = []
    min_length = float('inf')
 
    for i in range(len(rcs)):
        if not i % 2:
            customers.append((rcs[i], rcs[i + 1]))
 
    start = customers.pop(0)
    end = customers.pop(0)
 
    for perm in permutations(range(len(customers)), len(customers)):
        cum_length = 0
        cur_rc = start
         
        for customers_idx in perm:
            cum_length += cal_length(cur_rc, customers[customers_idx])
            cur_rc = customers[customers_idx]
 
            if cum_length >= min_length:
                break

        else:
            cum_length += cal_length(cur_rc, end)
            min_length = min(cum_length, min_length)
 
    print(f'#{tc} {min_length}')