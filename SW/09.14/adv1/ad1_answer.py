from itertools import combinations

def set_visited(r, c, visited):
    for i in range(N):
        if visited & (1<<i):
            continue

        if abs(r - home_info[i][0]) + abs(c - home_info[i][1]) <= home_info[i][2]:
            visited |= (1<<i)

    return visited

def calc_dist():
    total_distance = 0

    for home_idx in range(N):
        distance = float('inf')
        for charge_r, charge_c in pick_rcs:
            distance = min(distance, abs(charge_r - home_info[home_idx][0]) + abs(charge_c - home_info[home_idx][1]))
        total_distance += distance

    return total_distance

def dfs(count, idx):
    global visited
    # 종료조건
    if visited == (1<<N) - 1:
        results[count - 1] = min(results[count - 1], calc_dist())

    # count 1 만족하는지 확인 - 있으면 더 안 해봐도 됨
    if count == 2 or (count == 1 and results[0] < float('inf')):
        return

    for i in range(idx, 31 * 31):
        if i in not_i:
            continue

        r, c = i // 31, i % 31 
        i_visited = set_visited(r, c, visited)

        if i_visited != visited:
            backup, visited = visited, i_visited
            pick_rcs.append((r, c))
            dfs(count + 1, i + 1)
            visited = backup
            pick_rcs.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    visited = 0
    results = [float('inf'), float('inf')]

    not_i = set()
    home_info = []
    for _ in range(N):
        r, c, coverage = map(int, input().split())
        r += 15
        c += 15
        home_info.append((r, c, coverage))
        not_i.add(r * 31 + c)

    pick_rcs = []
    dfs(0, 0)

    answer = -1

    if results[0] != float('inf'):
        answer = results[0]
    elif results[1] != float('inf'):
        answer = results[1]

    print(f'#{tc} {answer}')