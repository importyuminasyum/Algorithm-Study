from collections import deque

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(start):
    que = deque()
    que.append(start)
    maze[start[0]][start[1]] = '1'

    while que:
        r, c = que.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc):
                continue

            if maze[nr][nc] == '1':
                continue
            
            if maze[nr][nc] == '3':
                return 1
            
            que.append((nr, nc))
            maze[nr][nc] = '1'

    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [
        list(input())
        for _ in range(N)
    ]

    # 0: 통로, 1: 벽, 2: 출발, 3: 도착
    for row in range(N):
        for col in range(N):
            if maze[row][col] == '2':
                start = (row, col)
            if maze[row][col] == '3':
                end = (row, col)

    print(f'#{tc} {bfs(start)}')

'''
bfs()
미로 탐색 
- 시작 좌표 큐에 넣기
- while que:
- pop
- 한 depth에 대해서 주변 가능한 좌표 탐색
- end 좌표면 return 1
- 아니면 모두 큐에 넣기
- 큐에 넣으면서 방문 체크

'''


