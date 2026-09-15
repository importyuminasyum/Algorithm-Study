T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lines = []
    answer = 0
    for _ in range(N):
        A, B = map(int, input().split())
        lines.append((A, B))

    for i in range(N):
        for j in range(i, N):
            if (lines[i][0] - lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
                answer += 1

    print(f'#{tc} {answer}')