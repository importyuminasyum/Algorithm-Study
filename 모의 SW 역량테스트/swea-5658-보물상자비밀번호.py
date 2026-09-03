# 3번 회전
# 필요한 것: 3번 회전할 동안 hexs rotate 한 결과를 담을 list [] - 문자열로 들어가기
# 1번 회전 - hexs.appendleft(hexs.pop())
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    n = N // 4
    hexs = list(input())
    results = [''.join(map(str, hexs[i : i + n])) for i in range(0, N, n)]

    for _ in range(n - 1): 
        hexs = deque(hexs)
        hexs.appendleft(hexs.pop())
        results.extend(''.join(map(str, list(hexs)[i : i + n])) for i in range(0, N, n))

    results = list(set(results))
    results.sort(key=lambda x: int(x, 16), reverse=True)

    print(f'#{tc} {int(results[K - 1], 16)}')