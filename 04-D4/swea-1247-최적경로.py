from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rcs = list(map(int, input().split()))
    rcs.append(rcs.pop(2))
    rcs.append(rcs.pop(2))  
    print(rcs)
    aligned_rcs = []
    min_length = float('inf')
    dist = [[0] * (N + 2) for _ in range(N + 2)]
    visited = [0] * N

    for i in range(0, N * 2 + 4, 2):
        aligned_rcs.append((rcs[i], rcs[i + 1]))

    for r in range(N + 2):
        for c in range(N + 2):
            dist[r][c] = abs(aligned_rcs[r][0] - aligned_rcs[c][0]) + abs(aligned_rcs[r][1] - aligned_rcs[c][1])

    # 회사, 집을 제외한 나머지 좌표들을 순열로 뽑아야 함
    for perm in permutations(range(1, N + 1), N):
        length = dist[0][perm[0]]

        for idx in range(N - 1):
            length += dist[perm[idx]][perm[idx + 1]]

        length += dist[perm[-1]][-1]
            
        min_length = min(length, min_length)

    print(f'#{tc} {min_length}')