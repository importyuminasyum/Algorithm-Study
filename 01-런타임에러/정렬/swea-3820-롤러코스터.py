from functools import cmp_to_key

def compare(x, y):
    a1, b1 = x
    a2, b2 = y

    xy = a2 * b1 + b2
    yx = a1 * b2 + b1

    if xy < yx:
        return -1
    elif xy > yx:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rails = []
    for _ in range(N):
        a, b = map(int, input().split())
        rails.append((a, b))

    rails.sort(key=cmp_to_key(compare))

    V = 1
    MOD = 1000000007
    for a, b in rails:
        V = (a * V + b) % MOD

    print(f'#{tc} {V}')