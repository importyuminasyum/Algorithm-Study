T = int(input())
for tc in range(1, T+1):
    S, P = map(int, input().split())

    for i in range(S):
        N, M = i, S - i
        if N * M == P:
            result = 'Yes'
            break
    else:
        result = 'No'

    print(f'#{tc} {result}')