from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    hexs = deque(input())
    result = set()
    n = N // 4
    # hexs를 리스트로 변환 후 회전, 슬라이싱해서 join, 16진수로 변환해서 result (set) 에 넣기
    for _  in range(n):
        for i in range(0, N, n):
            hex = ''.join(map(str, list(hexs)[i:i+n]))
            result.add(int(hex, 16))
        hexs.appendleft(hexs.pop())

    result = list(sorted(result, reverse=True))
    print(f'#{tc} {result[K - 1]}')