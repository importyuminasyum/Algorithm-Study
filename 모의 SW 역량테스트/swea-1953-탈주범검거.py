# 이동하기
# 거리가 L 미만인 터널의 칸 수 구하기 < 빈칸이 아니어야 함
# 터널 확인 어떻게?
# 함수로 숫자가 들어오면 direction 인덱스를 튜플로 묶어서 반환
# 이걸 반복문 이터레이터로 사용
# 한 depth에서 변환함수 사용해서 현재 노드에서 반복문 순회하면서 범위 내인 노드 append하기
# 시작점 한 개인 bfs
# backtracking? 음
# 각 초(depth)마다 누적 터널 개수 계산

from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우0 하1 좌2 상3

tunnel_directions = {
        1: (0, 1, 2, 3),
        2: (1, 3),
        3: (0, 2),
        4: (0, 3),
        5: (0, 1),
        6: (1, 2),
        7: (2, 3),
    }

def in_range(r, c, N, M):
    return 0 <= r < N and 0 <= c < M

def can_enter(direction, nr, nc): # 현재 방향 
    reverse_direction = (direction + 2) % 4
    return reverse_direction in tunnel_directions[under_map[nr][nc]]

def bfs(R, C):
    result, time = 1, 1
    que = deque()
    que.append((R, C))
    visited[R][C] = 1

    while que:
        if time >= L:
            return result
        
        for _ in range(len(que)):   
            cur_r, cur_c = que.popleft()
            directions = tunnel_directions[under_map[cur_r][cur_c]]
            
            for direction in directions:
                nr, nc = cur_r + dirs[direction][0], cur_c + dirs[direction][1]

                if in_range(nr, nc, N, M) and under_map[nr][nc] and not visited[nr][nc] and can_enter(direction, nr, nc):
                    que.append((nr, nc))
                    visited[nr][nc] = 1
                    result += 1

        time += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    visited = [
        [0] * M
        for _ in range(N)
        ]

    under_map = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    print(f'#{tc} {bfs(R, C)}')