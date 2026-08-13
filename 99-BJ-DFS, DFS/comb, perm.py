# 중복 순열
# depth = 지금까지 고른 숫자의 개수
def perm1(depth):
    # 중복 순열은 모든 노드에 대해 가능한 경우 출력
    # 종료조건 - depth가 M이 되었을 때 
    # 지금까지 뽑은 조합 출력 (print(pick_numbers))
    if depth == M:
        print(pick_numbers)
        return
    # for문을 N까지 돌면서 모든 노드
    # 방문 처리? 필요없음
    for i in range(len(numbers)):
        pick_numbers.append(numbers[i])
        perm1(depth + 1)
        pick_numbers.pop()

# 조합
# idx = 탐색을 시작할 인덱스 번호
def comb2(depth, idx):
    # 종료 조건: 중.순과 같음
    if depth == M:
        print(pick_numbers)
        return
    # 현재 인덱스: 조합에서 선택한 인덱스
    # for문을 현재 인덱스부터 N까지 돌면서 모든 노드
    # 선택하고 아래 노드 들어가기 (아래니까 depth 커지고 이미 선택한 노드 다시 선택 안 하니까 i도 + 1)
    # 방문 처리 안 해도 됨 왜? 애초에 중복 될 일 없음
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb2(depth + 1, i + 1)
        pick_numbers.pop()

# 중복 조합
def comb1(depth, idx):
    # 종료 조건: 중.순과 같음
    if depth == M:
        print(pick_numbers)
        return
    # 현재 인덱스: 조합에서 선택한 인덱스
    # for문을 현재 인덱스부터 N까지 돌면서 모든 노드
    # 선택하고 아래 노드 들어가기 (아래니까 depth 커지고 이미 선택한 노드 다시 선택 하니까 i도 포함해서 돌기)
    # 방문 처리 안 해도 됨 왜? 애초에 중복 될 일 없음
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb1(depth + 1, i)
        pick_numbers.pop()
    
# 순열
def perm2(depth):
    # 방문 처리 해야 함, 왜? 선택한 노드 빼고 모든 노드를 확인해야 하기 때문에
    # 종료조건: depth가 M일 때
    # pick_numbers 출력
    if depth == M:
        print(pick_numbers)
        return
    # n 돌면서 방문 체크 안 한 노드에 대해서만 들어가기 
    # 방문 체크 언제?
    # 들어가자마자
    # 언제 체크 초기화?
    # 종료할 때
    for i in range(len(numbers)):
        if visited[i]:
            continue

        visited[i] = 1
        pick_numbers.append(numbers[i])
        perm2(depth + 1)
        visited[i] = 0
        pick_numbers.pop()
    
N = 5
M = 3
numbers = [1,2,3,4,5]

pick_numbers = []
result = []

# 중복 순열
# perm1(0)

# 조합
# comb2(0, 0)

# 중복 조합
# comb1(0, 0)

# 순열
visited = [0]*len(numbers)
perm2(0)