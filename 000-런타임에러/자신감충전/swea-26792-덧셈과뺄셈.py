T = int(input())
for tc in range(1, T + 1):
    X, Y = map(int, input().split())
    print(f'#{tc} {(X + Y) / 2} {(X - Y) / 2}')