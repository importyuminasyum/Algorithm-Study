def tournament(start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    left = tournament(start, mid)
    right = tournament(mid + 1, end)

    return rcp(left, right)

def rcp(a, b):
    if cards[a] == cards[b]:
        return a

    if (
        (cards[a] == 1 and cards[b] == 3) or
        (cards[a] == 2 and cards[b] == 1) or
        (cards[a] == 3 and cards[b] == 2)
    ):
        return a

    return b
 
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    winner = tournament(0, N - 1)

    print(f'#{tc} {winner + 1}')