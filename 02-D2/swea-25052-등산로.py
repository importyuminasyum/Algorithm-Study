dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]
    longest_length = 0
    path_rcs = []

    for r in range(N):
        for c in range(N):
            path_rcs.append((r, c))
            lowest_r, lowest_c = 0, 0
            length = 0

            while path_rcs:
                cr, cc = path_rcs.pop()
                length += 1
                lowest_height = float('inf')

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc

                    if not in_range(nr, nc):
                        continue

                    if heights[nr][nc] < heights[cr][cc]:
                        if heights[nr][nc] < lowest_height:
                            lowest_height = heights[nr][nc]
                            lowest_r, lowest_c = nr, nc

                if lowest_height != float('inf'):
                    path_rcs.append((lowest_r, lowest_c))

                longest_length = max(longest_length, length)

    print(f'#{tc} {longest_length}')            

            
                