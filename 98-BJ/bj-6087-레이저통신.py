from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < H and 0 <= c < W

def bfs():
    # deque 생성
    # 초깃값: 시작점에 대해서 가능한 4방향 넣기
    # pop 하면서 while 문 시작
    # 종료조건: 다른 C 좌표 만나면
    # state에 대해서 nr, nc, count(사용횟수), direction
    # visited[nr][nc][direction] = count # 현재 방문한 누적 횟수 중 최솟값
    # 한 회차에서 가능한 것 - 방향 유지 / 90도 회전 '/' : + 1, '\': -1

    que = deque()
    # 초기 시작 좌표 세팅
    visited = [
        [[float('inf')] * 4 for _ in range(W)]
        for _ in range(H)
    ]

    start_r, start_c = connect_rcs[0]
    end_r, end_c = connect_rcs[1]

    for dir in range(4):
        nr, nc = start_r + dirs[dir][0], start_c + dirs[dir][1]
        if in_range(nr, nc) and board[nr][nc] != '*':
            visited[nr][nc][dir] = 0
            que.append((nr, nc, dir))

    while que:
        cur_r, cur_c, dir = que.popleft()
        count = visited[cur_r][cur_c][dir]

        if (cur_r, cur_c) == (end_r, end_c):
            return count

        for turn in (0, 1, -1):
            new_dir = (dir + turn) % 4
            nr, nc = cur_r + dirs[new_dir][0], cur_c + dirs[new_dir][1]

            new_count = count
            
            if turn != 0:
                new_count += 1

            if in_range(nr, nc) and board[nr][nc] != '*':
                if new_count < visited[nr][nc][new_dir]:
                    visited[nr][nc][new_dir] = new_count
                    if turn == 0:
                        que.appendleft((nr, nc, new_dir))
                    else:
                        que.append((nr, nc, new_dir))

W, H = map(int, input().split())
board = [
    list(input())
    for _ in range(H)
]
connect_rcs = []
min_laser = float('inf')

for row in range(H):
    for col in range(W):
        if board[row][col] == 'C':
            connect_rcs.append((row, col))

print(bfs())
