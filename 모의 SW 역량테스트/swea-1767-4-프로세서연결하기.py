
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def dfs(depth, cul_core, cul_length):
    global max_core, min_length

    remaining_cores = len(core_rcs) - depth
    if remaining_cores + cul_core < max_core:
        return

    if remaining_cores + cul_core == max_core and cul_length >= min_length:
        return

    if depth == len(core_rcs):
        if cul_core > max_core:
            max_core = cul_core
            min_length = cul_length

        elif cul_core == max_core:
            min_length = min(cul_length, min_length)
        
        return

    candidates = []

    core_r, core_c = core_rcs[depth]

    for dr, dc in dirs:
        length = check_link(core_r, core_c, dr, dc)

        if length:
            candidates.append((length, dr, dc))

    candidates.sort()
    
    for length, dr, dc in candidates:
        set_cable(core_r, core_c, dr, dc, 1)
        dfs(depth + 1, cul_core + 1, cul_length + length)
        set_cable(core_r, core_c, dr, dc, 0)

    dfs(depth + 1, cul_core, cul_length)


def set_cable(r, c, dr, dc, value):
    nr, nc = r + dr, c + dc

    while in_range(nr, nc, N):
        maxynos[nr][nc] = value
        nr, nc = nr + dr, nc + dc

  
def check_link(r, c, dr, dc):
    nr, nc = r + dr, c + dc
    length = 0

    while in_range(nr, nc, N):
        if maxynos[nr][nc]:
            return 0

        length += 1
        nr, nc = nr + dr, nc + dc
        
    return length


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maxynos = [
        list(map(int, input().split()))
        for _ in range(N)
    ]
    core_rcs = []
    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if maxynos[row][col]:
                core_rcs.append((row, col))
    max_core, min_length = 0, float('inf')

    dfs(0, 0, 0)

    print(f'#{tc} {min_length}')