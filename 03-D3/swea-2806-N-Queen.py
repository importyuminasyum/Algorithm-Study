# 각 행에 퀸을 하나 둔다고 생각하고 depth를 N으로 잡기
# 탈출 조건: row가 N에 도달했을때
# col을 돌면서
# 행이 같거나 대각선 사이가 아니면 내려가기 (재귀)
# 아니면 계속 내려가기
# 내려갈때 줄건 뭘까? 다음 row
def check(row, col):
    for prev_row in range(row):
        prev_col = queen[prev_row]
        # 같은 열인지
        if prev_col == col:
            return False
        # 대각선인지
        if abs(col - prev_col) == abs(row - prev_row):
            return False
    return True

def dfs(row):
    global count

    if row == N:
        count += 1
        return
    
    for col in range(N):
        if check(row, col):
            queen[row] = col
            dfs(row + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    queen = [-1] * N # 각 인덱스(행)마다 퀸을 놓은 열이 담길 것
    count = 0

    dfs(0)
    print(f'#{tc} {count}')
    