'''
1
dist가 < C인 점에 대해서 성능을 3차원 배열에 넣기 - 배열로
만약에 겹치면? 성능 배열 append 해


BC1, BC2 - 두 개가 겹치는 지점에 두 사용자가 같은 시간에 들어왔다면
1) 각각 더 큰 성능 가진 애를 나눠 가지기
2) BC1, BC2 갖기

일단 deque에 이동경로 넣고
while que
하나씩 pop하면서
dir = que.pop()
nr, nc = cr + dirs[dir][0], cc + dirs[dir][1]

이제 이 좌표가 어떤 충전지역에 속해있는지 확인
check_BC(nr, nc) - 출력 - 인덱스 값을 튜플로2
check_BC(nr2, nc2) - 튜플로

만약 둘이 겹치면 비교
- 그 담에 최댓값 넣기

안 겹치면 각각 확인
그 튜플 순회하면서
- 첫 번째 인덱스 성능
- 두 번째 인덱스 성능
...
- 비교하고 최댓값 넣기


'''
dirs = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]

def check_BC(r, c):

    in_range_AP = []

    for i in range(A):
        if abs(r - AP[i][1]) + abs(c - AP[i][0]) <= AP[i][2]:
            in_range_AP.append((i, AP[i][3]))

    return in_range_AP

def cal_max_charge_level():
    global result

    ar, ac = 1, 1
    br, bc = 10, 10
    
    for t in range(M + 1):
        perf_A, perf_B = check_BC(ar, ac) + [(-1, 0)], check_BC(br, bc) + [(-2, 0)]

        if perf_A or perf_B:
            max_charge = 0
            for a_idx, a_power in perf_A:
                for b_idx, b_power in perf_B:
                    if a_idx == b_idx:
                        charge = a_power
                    else:
                        charge = a_power + b_power

                    max_charge = max(max_charge, charge)

        result += max_charge

        if t == M:
            break

        ar += dirs[A_info[t]][0]
        ac += dirs[A_info[t]][1]

        br += dirs[B_info[t]][0]
        bc += dirs[B_info[t]][1]

T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    A_info = list(map(int, input().split()))
    B_info = list(map(int, input().split()))

    AP = [list(map(int, input().split())) for _ in range(A)]

    result = 0
    cal_max_charge_level()
    print(f'#{tc} {result}')

        