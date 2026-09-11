'''
몇개의 색을 다시 칠해서 
새로 칠해야 하는 칸의 개수를 최소로 만들 수 있을까?
투 포인터로 top bottom 정하기
인덱스를 분류해야 함
top / middle / bottom

그 인덱스를 range로 행 돌면서 value 값에 대해서 
value count하고 M에서 빼서 return

''' 
def count_coloring(idxs, value):
    idx1, idx2 = idxs
    coloring_value_count = 0

    for i in range(idx1, idx2):
        coloring_value_count += M - gonfalon[i].count(value)

    return coloring_value_count

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    gonfalon = [list(input()) for _ in range(N)]
    min_coloring_count = float('inf')

    for top in range(1, N - 1):
        for bottom in range(top + 1, N):
            top_w = (0, top)
            middle_b = (top, bottom)
            bottom_r = (bottom, N)

            count = count_coloring(top_w, 'W') + count_coloring(middle_b, 'B') + count_coloring(bottom_r, 'R')
            min_coloring_count = min(count, min_coloring_count)

    print(f'#{tc} {min_coloring_count}')