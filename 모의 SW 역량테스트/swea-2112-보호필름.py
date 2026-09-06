'''
def performance_test(films):

    가능하면: 1
    불가능하면: 0
    
처음 성능검사 해보기
가능하면 0 끝
불가능하면 확인해봐야 함

최소 2번 시행해야 하니까

def dfs(depth(투약 횟수), films):
    if performance_test(films):
        if min_input == 1:
            return 2
            
        min_input = min(min_input, depth)
        
        return

    for row in range(D):
        backup_row = copy.deepcopy(films[row])
        # A 약물 적용
        medication(row, films[row], 1)
        dfs(depth + 1, films)
        # B 약물 적용
        medication(row, films[row], 0)
        dfs(depth + 1, films)
        # 복구
        medication(row, backup_row, -1)
        dfs(depth + 1, films)

def medication(row_idx, selected_D, value):
    if value == -1:
        for col in range(W):
            films[row_idx][col] = selected_D[col]
    
    for col in range(W):
        films[row_idx][col] = value
            
    return

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

        
처음에 들어오자마자 그냥 확인
    성능 검사 - 되면 return 끝

    depth == 1 일 때 되면 return 2

    안되면 - 계속 해야함

    한 번 시도에서 할 수 있는 것:
        한 행을 선택, value 선택해서 보내기
        
        투약 함수(행 선택, value(A / B))
        
        1번 A로 / B로
        2번 A로 / B로


'''

def performance_test(cur_films):
    for col in range(W):
        count = 1

        for row in range(1, D):
            if cur_films[row][col] == cur_films[row - 1][col]:
                count += 1
            else:
                count = 1

            if count >= K:
                break

        if count < K:
            return False
        
    return True

def dfs(row, count):
    global min_input

    if count >= min_input:
        return
    
    if performance_test(films):
        min_input = count
        return 

    if row == D:
        return

    dfs(row + 1, count)

    backup = films[row][:]

    films[row] = [0] * W
    dfs(row + 1, count + 1)

    films[row] = [1] * W
    dfs(row + 1, count + 1)

    films[row] = backup

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
    min_input = float('inf')

    dfs(0, 0)

    print(f'#{tc} {min_input}')