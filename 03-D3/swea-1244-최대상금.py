# depth = 교환횟수
# 종료조건
# depth가 N일 때
# 같은 depth에서 같은 숫자 상태에 도달하면, 지금까지 어떤 경로로 왔든 이후 가능한 교환 트리는 동일
# 조합짜서 swap 하기
# 받은 문자를 숫자로 만들어서 i, j 가능한 조합 swap 하고 재귀
# 같은 depth에 대해서 탐색한 숫자는 리스트에 넣고 매번 확인해서 있으면 지나치기
# number, numbers : 대상 숫자, ㅇ
def dfs(depth):
    global max_number

    state = int(''.join(number))

    # 중복 확인 - 중복이면 탐색 안 함
    if state in visited[depth]:
        return

    visited[depth].add(state)

    # 횟수 충족하면
    if depth == N:
        max_number = max(max_number, state)
        return 
    
    # 모든 i, j 인덱스에 대해서 숫자 바꾸고 재귀, 다시 원상복구 반복 
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            number[i], number[j] = number[j], number[i]
            dfs(depth + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T + 1):
    max_number = float('-inf')
    number, N = input().split()
    number = list(number)
    N = int(N)
    visited = [set() for _ in range(N + 1)] # 각 행에 대해서
    dfs(0)
    print(f'#{tc} {max_number}')