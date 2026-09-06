def performance_test(films):
    # 모든 열이 통과하면 통과, 중간에 안되는 거 있으면 그냥 return 0
    possible_count = 0
    for col in range(W):
    # 열 우선 순회
        # 한 행에 대해서 두가지 중 하나만 만족하면 possible count += 1
        state = 0
        for value in (0, 1):
            # 0 찾기
            k_count = 0

            for row in range(D):
                if k_count >= K:
                    state += 1
                    break
            
                if films[row][col] == value:
                    k_count += 1
            
                else:
                    k_count = 0

            if k_count >= K:
                state += 1

        if state:
            possible_count += 1

    if possible_count == W:
        return 1

    return 0

def medication(row_idx, selected_D, value, cur_films):
    if value == -1: # 원상복구 해야 함
        for col in range(W):
            cur_films[row_idx][col] = selected_D[col]
        return cur_films
    
    for col in range(W):
        cur_films[row_idx][col] = value
    return cur_films
import copy
T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    # D: 두께
    # W: 가로 크기
    films = [
        list(map(int, input().split()))
        for _ in range(D)
    ]
    # A: 0, B: 1
    min_input = 0

    copy_films = copy.deepcopy(films[0])
    print(f'#{tc} {medication(0, films[0], 0, films)}')
    print(films)

    print(f'#{tc} {medication(0, copy_films, -1, films)}')
    print(films)

