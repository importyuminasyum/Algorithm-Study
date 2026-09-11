from collections import deque
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    text = list(input().split())
    if not N % 2:
        A, B = deque(text[:N // 2]), deque(text[N // 2:])
    else:
        A, B = deque(text[:N // 2 + 1]), deque(text[N // 2 + 1:])

    result = []

    for i in range(N):
        if not i % 2:
            result.append(A.popleft())
            continue

        result.append(B.popleft())

    print(f'#{tc} {" ".join(result)}')