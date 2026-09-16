from collections import deque

def bfs():
    q = deque()
    q.append(N)
    visited.add(N)
    count = 0

    while q:
        for _ in range(len(q)):
            num = q.popleft()

            if num == M:
                return count

            for next_num in (num + 1, num - 1, num * 2, num - 10):
                if next_num in visited:
                    continue

                if next_num > 1000000 or next_num < 0:
                    continue
                
                q.append(next_num)
                visited.add(next_num)

        count += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    visited = set()
    print(f'#{tc} {bfs()}')