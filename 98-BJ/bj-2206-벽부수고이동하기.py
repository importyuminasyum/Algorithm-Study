dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우 하 좌 상

def in_range(r, c):
    return 0 <= r < N and 0 <= c < M

def dfs(depth, r, c):
    global result, min_length, chance

    if r == N - 1 and c == M - 1:
        result.append(min_length)
        return

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if in_range(nr, nc):
            if map[nr][nc] == 1:
                if chance: # 기회를 쓰는 지점
                    chance = 0
                    min_length += 1
                    map[nr][nc] = 2 # 이동했다는 뜻
                    dfs(depth + 1, nr, nc)
                    min_length -= 1
                    map[nr][nc] = 1
                    chance = 1
                else: # 기회가 없는 지점, 이 시점에서 더 이상 갈 수 없음 
                    continue

            elif map[nr][nc] == 0:
                min_length += 1
                map[nr][nc] = 2 # 이동했다는 뜻
                dfs(depth + 1, nr, nc)
                min_length -= 1
                map[nr][nc] = 0

N, M = map(int, input().split()) # 종료지점
result = []
min_length = 1
chance = 1

map = [
    list(map(int, input()))
    for _ in range(N)
]

map[0][0] = 2
dfs(0, 0, 0)

if result:
    print(min(result))
else:
    print(-1)