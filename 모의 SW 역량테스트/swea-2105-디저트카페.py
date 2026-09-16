'''
디저트 카페
N * N 디저트 카페들이 있음
값: 디저트의 종류
대각선 방향으로 움직일 수 있음
어느 한 카페에서 출발해서 대각선 방향으로 움직이고 사각형 모양을 그리면서 출발한 카페로 돌아와야 함
카페 투어 중에 같은 숫자의 디저트를 팔고 있는 카페가 있으면 안 됨
- 또 나오면 제껴
- 하나의 카페에서 디저트를 먹는 것도 안 됨
- 왔던 길을 다시 돌아가는 것도 안 됨

- 디저트를 되도록 많이 먹으려고 함
T
N
N * N - 디저트 종류

출력
max_dessert
- 디저트를 가장 많이 먹을 때의 디저트 수
- 디저트를 먹을 수 없는 경우 -1

'''

dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

def in_range(r, c, a, b):
    return 0 <= r < N and 0 <= c < N and r + a + b < N and c + a < N and c - b >= 0

def dessert_search():
    global max_dessert

    for r in range(N):
        for c in range(N):
            for a in range(1, N):
                for b in range(1, N):
                    if not in_range(r, c, a, b):
                        continue

                    selected_dessert = set()
                    cr, cc = r, c        

                    valid = True      

                    for dir in range(4):
                        length = a

                        if dir % 2:
                            length = b

                        for _ in range(length):
                            nr, nc = cr + dirs[dir][0], cc + dirs[dir][1]

                            if rocation[nr][nc] in selected_dessert:
                                valid = False
                                break

                            selected_dessert.add(rocation[nr][nc])
                            cr, cc = nr, nc

                        if not valid:
                            break

                    if valid:
                        max_dessert = max(len(selected_dessert), max_dessert)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rocation = [list(map(int, input().split())) for _ in range(N)]
    max_dessert = -1
    dessert_search()
    print(f'#{tc} {max_dessert}')
