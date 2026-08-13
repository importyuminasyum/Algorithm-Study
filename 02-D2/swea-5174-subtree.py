# 5 1
# 2 1 2 5 1 6 5 3 6 4
# 1: 6, 2: 1, 5, 5: 3, 6:4
# 일단 하나의 리스트로 받고, 부모 자식 쌍으로 구분해서 분류해야 함
# 2, 3, 1, 5, 6 parents
# 1, 5, 6, 3, 4 childs
# i(인덱스)로 순회하면서 parent[i] 2가 키, child[i]를 추가 (value)
# 받은 값을 키로 하는 딕셔너리를 순회하면서
# 각 키를 값으로 넣기
# 종료 조건: 딕셔너리 키가 없으면 return
from collections import defaultdict

def dfs(parent_node):
    global answer

    if not parent_node in adj_list:
        return answer

    for child_node in adj_list[parent_node]:
        answer += 1
        dfs(child_node)
            

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    nodes = list(map(int, input().split()))
    parents, childs = [], []
    adj_list = defaultdict(list)
    answer = 1
     
    for i in range(E * 2):
        if i % 2 == 0:
            parents.append(nodes[i])
        else:
            childs.append(nodes[i])

    for i in range(E):
        adj_list[parents[i]].append(childs[i])

    dfs(N)
    print(f'#{tc} {answer}')