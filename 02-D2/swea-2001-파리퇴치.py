# 1. M * M 최댓값 행렬 만들기
# 출력: 최댓값이 담긴 M * M 행렬에서 최댓값 
# 아니면 그냥 최댓값 갱신
# fly_catcher(M): 들어온 배열에 대해서 이차원 for문을 돌면서 최댓값 구하기
# 이차원 for문 돌면서 fly_catcher(M) 값 최댓값에 넣고 갱신하기
def fly_catcher(i, j, M):
    total = 0
    for row in range(M):
        for col in range(M):
            total += board[i + row][j + col]
    return total

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_flies = 0
    board = []
    for i in range(N):
        board.append(list(map(int, input().split())))

    for row in range(N - M):
        for col in range(N - M):
            max_flies = max(max_flies, fly_catcher(row, col, M))      

    print(f'#{tc} {max_flies}')