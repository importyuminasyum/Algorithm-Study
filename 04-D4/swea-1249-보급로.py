import heapq

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def dijkstra():
    end = (N - 1, N - 1)

    dist = [[float('inf')] * N for _ in range(N)]
    dist[0][0] = 0

    # heapq.heappush(pq, (새로운누적비용(현재누적비용 + 이번 비용), 행, 열))
    # heapq.heappop(pq)

    pq = []
    heapq.heappush(pq, (0, 0, 0))

    while pq:
        # 최소비용 먼저 pop
        cur_cost, r, c = heapq.heappop(pq)
        
        # 현재 pop한 상태가 유효한가?
        if cur_cost > dist[r][c]:
            continue

        if (r, c) == end:
            return cur_cost

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc

            if not in_range(nr, nc):
                continue

            new_cost = cur_cost + field[nr][nc]
            # 다음 칸을 더 싸게 갈 수 있는가?
            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heapq.heappush(pq, (new_cost, nr, nc))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)]

    print(f'#{tc} {dijkstra()}')