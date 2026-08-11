def dfs(idx, score, cal):
    # 모든 원소에 대해서 넣을건지 말건지 두가지 선택지
    # 처음 원소부터 시작(N번)해서 넣는 dfs 안넣는 dfs
    # 그때 칼로리가 L보다 커지면 탈출, depth가 N개 도달하면 탈출
    # 누적 칼로리 필요
    # 키를 순회하면서 값을 누적하는 방식
    # 키를 
    # 100 - 300 - 250- 500 -400 가는 선택지
    #  x - 300 - 250- 500- 400 가는 선택지를 매 분기마다
    # 탈출 지점
    global max_score

    if cal > L:
        return

    if idx > N:
        max_score = max(max_score, score)
        print(max_score)
        return
    
    dfs(idx+1, score, cal)
    dfs(idx+1, score + like[idx], cal + calorie[idx])

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for tc in range(1, T + 1):
    N, L = map(int, input().split())
    like, calorie = [0]*(N+1), [0]*(N+1)
    max_score = float('-inf')

    for i in range(1, N+1):
        like[i], calorie[i] = map(int, input().split())

    print(f'#{tc}', end='')
    dfs(1, 0, 0)

    