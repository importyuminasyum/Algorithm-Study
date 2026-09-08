'''가장 멀리갈 수 있는 칸 수를 셈. 한 길만 제시하면 됨. 
조건) 본인 이상인 곳은 갈 수 없음. 자기보다 작은 애들 중에 여러 곳이 있으면 가장 최소인 곳으로 감.
이 때 최대 몇 칸 까지 갈 수 있는가가 문제. 상하좌우로 떨어질 수 있음
출발지? 모름. 모든 출발지를 다 해봤을 때 칸 수를 다 세는게 목적.
'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            move_info = [(field[i][j], i, j)]
            count = 0

            while move_info:
                cur_value, cur_r, cur_c = move_info.pop()
                count += 1

                temp_value = []
                temp_info = []
                for dr, dc in dirs:
                    nr, nc = cur_r + dr, cur_c + dc
                    if in_range(nr, nc) and field[nr][nc] < cur_value:
                        temp_value.append(field[nr][nc])
                        temp_info.append((nr, nc))

                for idx in range(len(temp_info)):
                    if temp_value[idx] == min(temp_value):
                        move_info.append((temp_value[idx], temp_info[idx][0], temp_info[idx][1]))
                        
            result = max(count, result)

    print(f'#{tc} {result}')
