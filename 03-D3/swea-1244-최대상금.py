# depth = 교환횟수
# 종료조건
# depth가 N일 때
# 88832 같은 경우 (겹치는 숫자가 있을 경우)에는 이후 가지가 완전히 동일해짐
# 조합짜서 swap 하기
# 받은 문자를 숫자로 만들어서 i, j 가능한 조합 swap 하고 재귀
# 같은 depth에 대해서 탐색한 숫자는 리스트에 넣고 매번 확인해서 있으면 지나치기
# number, numbers : 대상 숫자, ㅇ
def dfs(depth):
    global max_number
    # 중복 확인 - 중복이면 탐색 안 함
    if number in visited[depth]:
        return

    # 횟수 충족하면
    if depth == N:
        max_number = max(max_number, number)
        return 
        
    visited[depth] = number
    
    # 모든 i, j 인덱스에 대해서 숫자 바꾸고 재귀, 다시 원상복구 반복 
    for i in range(N):
        for j in range(i + 1, N):
            number[i], number[j] = number[j], number[i]
            dfs(depth + 1)
            number[i], number[j] = number[j], number[i]

T = int(input())
for tc in range(1, T + 1):
    max_number = float('-inf')
    number, N = input().split()
    N = int(N)
    visited = [set() for _ in range(10001)] # 각 행에 대해서
    dfs(0)
    print(f'#{tc} {max_number}')