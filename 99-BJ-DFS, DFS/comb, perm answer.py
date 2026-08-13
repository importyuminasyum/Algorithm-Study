# 중복 순열
# depth = 지금까지 고른 숫자의 개수
def perm1(depth):
    if depth == M:
        print(pick_numbers)
        return

    # 아직 M개 미만 골랐으므로 골라줘야 함
    for i in range(len(numbers)):
        pick_numbers.append(numbers[i])
        perm1(depth+1)
        pick_numbers.pop()

# idx = 탐색을 시작할 인덱스 번호
def comb2(depth, idx):
    if depth == M:
        print(pick_numbers)
        return
    # i != idx, i = 현재 고른 인덱스 번호
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb2(depth+1, i+1)
        pick_numbers.pop()

def comb1(depth, idx):
    if depth == M:
        print(pick_numbers)
        return
    # i != idx, i = 현재 고른 인덱스 번호
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb1(depth+1, i)
        pick_numbers.pop()

def perm2(depth):
    if depth == M:        
        print(pick_numbers)
        return

    # 아직 M개 미만 골랐으므로 골라줘야 함
    for i in range(len(numbers)):
        if visited[i]:
            continue

        visited[i] = 1
        pick_numbers.append(numbers[i])
        perm2(depth+1)
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