T = int(input())
for tc in range(1, T+1):
    N, S = map(int, input().split())
    rcs = list(map(int, input().split()))
    min_length = float('inf')

    rcs.insert(0, S)
    rcs.sort()

    start_idx = rcs.index(S)

    if start_idx == 0:
        length = 0
        for i in range(start_idx, N):
            length += abs(rcs[i] - rcs[i + 1])
        print(f'#{tc} {length}')

    elif start_idx == N:
        length = 0
        for i in range(start_idx, 0, -1):
            length += abs(rcs[i] - rcs[i - 1])
        print(f'#{tc} {length}')

    else:
        length1, length2 = 0, 0

        for i in range(start_idx, N):
            length1 += abs(rcs[i] - rcs[i + 1])

        length1 += abs(rcs[-1] - rcs[start_idx - 1])

        for i in range(start_idx - 1, 0, -1):
            length1 += abs(rcs[i] - rcs[i - 1])

        for i in range(start_idx, 0, -1):
            length2 += abs(rcs[i] - rcs[i - 1])

        length2 += abs(rcs[0] - rcs[start_idx + 1])

        for i in range(start_idx + 1, N):
            length2 += abs(rcs[i] - rcs[i + 1])

        min_length = min(length1, length2)
        print(f'#{tc} {min_length}')