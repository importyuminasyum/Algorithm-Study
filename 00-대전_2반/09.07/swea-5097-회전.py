from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word = deque(input().split())

    for _ in range(M):
        forward_num = word.popleft()
        word.append(forward_num)

    print(word[0])